import os
import time
import redis
import TestLanguage
from cpu import Cpu


class VMWorker():

    redis_client = redis.StrictRedis(host="128.199.43.95", port=6379, db=0)
    pid = os.getpid()

    def __init__(self):
        pass

    def compile_sourcecode(self, sourcecode, userid):

        self.redis_client.publish("console:{0}".format(userid), "Compiling source code into bytecodes.\r\n")

        # Store sourcecode in Redis ("sourcecode:{userid}").
        self.redis_client.set("sourcecode:{0}".format(userid), sourcecode)

        # Compile sourcecode written in browser. Store in Redis ("bytecodes:{userid}").
        bytecodes = TestLanguage.compile_code(sourcecode)
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

        self.redis_client.publish("console:{0}".format(userid),
                                  "Worker {0} deserialized cpu and will execute some code.\r\n".format(self.pid))

        # Execute.
        counter = 0
        try:
            while True:
                # Execute one step.
                counter += 1

                if cpu.counter > 10000:
                    self.redis_client.publish("console:{0}".format(userid),
                                              "Program has executed a maximum of 10.000 instructions.\r\n")
                    self.redis_client.lrem("commandqueue", -1000, "compile:{0}".format(userid))
                    self.redis_client.lrem("commandqueue", -1000, "compile-and-run:{0}".format(userid))
                    self.redis_client.lrem("commandqueue", -1000, "continue:{0}".format(userid))
                    raise "Max number of instructions reached."

                output = cpu.execute_step()
                if output:
                    self.redis_client.publish("console:{0}".format(userid), output)

                # Publish not every single step, that takes too long.
                if counter % 20 == 0:
                    # TODO: Output mem properly.
                    output = cpu.get_mem()
                    self.redis_client.publish("mem:{0}".format(userid), output)

                # TODO: Timeslices instead of op counters? Simple to implement!

                if counter >= 200:
                    # Serialize cpu.
                    self.redis_client.set("cpu:{0}".format(userid), cpu.serialize_cpu())

                    # Send queuecommand to continue executing.
                    # TODO: Separate command, not compile-and-run!!!
                    self.redis_client.lrem("commandqueue", -1000, "compile:{0}".format(userid))
                    self.redis_client.lrem("commandqueue", -1000, "compile-and-run:{0}".format(userid))
                    self.redis_client.lrem("commandqueue", -1000, "continue:{0}".format(userid))
                    self.redis_client.lpush("commandqueue", "continue:{0}".format(userid))

                    self.redis_client.publish("console:{0}".format(userid),
                                              "Worker {0} serialized cpu and relinquished it.\r\n".format(self.pid))

                    # A useless sleep just to potentially let another worker grab this job first.
                    time.sleep(1)
                    break

        except Exception:
            self.redis_client.publish("console:{0}".format(userid), "Execution complete.\r\n")
            print("Program ended. Crash?")
            pass

        finally:
            pass

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
                        except Exception as ex:
                            self.redis_client.publish("console:{0}".format(userid),
                                                      "Syntax error: {0}.\r\n".format(ex))

                        # Run the program.
                        self.run_some_steps(userid)

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
