import os
import time
import redis
from TinyLanguage import TinyLanguage
from cpu import Cpu


class VMWorker():

    redis_client = redis.StrictRedis(host="redis.topholt.com", port=6379, db=0)
    pid = os.getpid()

    def __init__(self):
        pass

    def compile_sourcecode(self, sourcecode, userid):

        self.redis_client.publish("console:{0}".format(userid), "Compiling source code into bytecodes.\r\n")

        # Store sourcecode in Redis ("sourcecode:{userid}").
        self.redis_client.set("sourcecode:{0}".format(userid), sourcecode)

        # Compile sourcecode written in browser. Store in Redis ("bytecodes:{userid}").
        bytecodes = TinyLanguage.compile_code(sourcecode)
        self.redis_client.set("bytecodes:{0}".format(userid), bytecodes)

        self.redis_client.publish("console:{0}".format(userid), "Compilation successful.\r\n")

        # Create the CPU. Store as serialized in Redis ("cpu:{userid}").
        cpu = Cpu(bytecodes, 512, 128, 0, 384)
        self.redis_client.set("cpu:{0}".format(userid), cpu.serialize_cpu())

        # Get disassembly and publish on "disassembly:{userid}" channel.
        disassembly = cpu.get_disassembly()
        self.redis_client.publish("disassembly:{0}".format(userid), disassembly)

        # Publish the bytecodes on the "bytecodes:{userid}" channel.
        self.redis_client.publish("bytecodes:{0}".format(userid), bytecodes)

    def run_some_steps(self, userid):
        # Deserialize and get ready to execute.
        serialized_cpu = self.redis_client.get("cpu:{0}".format(userid))
        cpu = Cpu([], 512, 128, 0, 384)
        cpu.deserialize_cpu(serialized_cpu)

        # Execute.
        self.redis_client.publish("console:{0}".format(userid),
                                  "Worker {0} deserialized cpu and will execute some code.\r\n".format(self.pid))
        counter = 0
        try:
            console_output = ""
            while True:
                # Execute one step.
                counter += 1

                if cpu.counter > 10000:
                    self.redis_client.publish("console:{0}".format(userid),
                                              "Program exceeded the maximum of 10.000 instructions, stopping.\r\n")
                    self.redis_client.lrem("commandqueue", -1000, "compile:{0}".format(userid))
                    self.redis_client.lrem("commandqueue", -1000, "compile-and-run:{0}".format(userid))
                    self.redis_client.lrem("commandqueue", -1000, "continue:{0}".format(userid))
                    break

                # Get console and mem output from cpu.
                console_output = console_output + cpu.execute_step()
                mem_output = cpu.get_mem()

                # Publish not every single step, that takes too long.
                if counter % 50 == 0:
                    self.redis_client.publish("mem:{0}".format(userid), mem_output)
                if counter % 200 == 0:
                    self.redis_client.publish("console:{0}".format(userid), console_output)
                    console_output = ""
                if counter >= 2000:
                    # Serialize cpu.
                    self.redis_client.set("cpu:{0}".format(userid), cpu.serialize_cpu())

                    # Send queuecommand to continue executing.
                    self.redis_client.lrem("commandqueue", -1000, "compile:{0}".format(userid))
                    self.redis_client.lrem("commandqueue", -1000, "compile-and-run:{0}".format(userid))
                    self.redis_client.lrem("commandqueue", -1000, "continue:{0}".format(userid))
                    self.redis_client.lpush("commandqueue", "continue:{0}".format(userid))
                    break

        except StopIteration:
            self.redis_client.publish("console:{0}".format(userid), "Program execution finished.")

        except Exception:
            print("Program ended.")

        finally:
            # Output any remaining console output.
            self.redis_client.publish("mem:{0}".format(userid), mem_output)
            self.redis_client.publish("console:{0}".format(userid), console_output)
            self.redis_client.publish("console:{0}".format(userid),
                                      "Worker {0} serialized cpu and relinquished it.\r\n".format(self.pid))

    def start_worker(self):
        try:
            counter = 0

            while True:
                counter += 1

                # Pop command from command queue in Redis.
                command_string = self.redis_client.rpop("commandqueue")
                if command_string:
                    command = str.split(command_string, ':')
                    if command[0] == "compile":
                        userid = command[1]
                        try:
                            sourcecode = self.redis_client.get("sourcecode:{0}".format(userid))
                            self.compile_sourcecode(sourcecode, userid)
                        except Exception as ex:
                            self.redis_client.publish("console:{0}".format(userid),
                                                      "Syntax error: {0}.\r\n".format(ex))

                    elif command[0] == "compile-and-run":
                        userid = command[1]
                        try:
                            sourcecode = self.redis_client.get("sourcecode:{0}".format(userid))
                            self.compile_sourcecode(sourcecode, userid)

                            # Run the program.
                            self.run_some_steps(userid)

                        except Exception as ex:
                            self.redis_client.publish("console:{0}".format(userid),
                                                      "Syntax error: {0}.\r\n".format(ex))

                    elif command[0] == "continue":
                        # Continue the program.
                        userid = command[1]
                        self.run_some_steps(userid)

                # Sleep for a while.
                time.sleep(0.1)

        except Exception as ex:
            # TODO: Log error here.
            print("VMWorker thread crashed: " + str(ex))

        finally:
            print("Exiting VMWorker thread.")
            exit(0)
