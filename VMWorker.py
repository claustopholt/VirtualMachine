import os
import time
import redis
import TestLanguage
from cpu import Cpu


class VMWorker():

    redis_client = redis.StrictRedis(host="128.199.43.95", port=6379, db=0)

    def __init__(self):
        pass

    def compile_sourcecode(self, sourcecode, userid):
        # Store sourcecode in Redis ("sourcecode:{userid}").
        self.redis_client.set("sourcecode:{0}".format(userid), sourcecode)

        # Compile sourcecode written in browser. Store in Redis ("bytecodes:{userid}").
        bytecodes = TestLanguage.compile_code(sourcecode)
        self.redis_client.set("bytecodes:{0}".format(userid), bytecodes)

        # Create the CPU. Store as serialized in Redis ("cpu:{userid}").
        cpu = Cpu(bytecodes, 512, 128, 0, 384)
        self.redis_client.set("cpu:{0}".format(userid), cpu.serialize_cpu())

        # Get disassembly and publish on "disassembly:{userid}" channel.
        disassembly = cpu.get_disassembly()
        self.redis_client.publish("disassembly:{0}".format(userid), disassembly)

        # Publish the bytecodes on the "bytecodes:{userid}" channel.
        self.redis_client.publish("bytecodes:{0}".format(userid), bytecodes)

    def start_worker(self):
        try:
            counter = 0
            pid = os.getpid()

            while True:
                counter += 1

                # Pop command from command queue in Redis.
                command_string = self.redis_client.rpop("commandqueue")
                if command_string:
                    command = str.split(command_string, '|||')
                    print("Worker {0} got command from Redis: {1}".format(pid, command))
                    if command[0] == "compile":
                        try:
                            userid = command[1]
                            sourcecode = command[2]
                            self.compile_sourcecode(sourcecode, userid)
                        except Exception as ex:
                            #return "Syntax error: " + str(ex), 400
                            # TODO: Send message to user that a failure occurred.
                            print("ERROR!!!")

                    elif command[0] == "compile-and-run":
                        try:
                            userid = command[1]
                            sourcecode = command[2]
                            self.compile_sourcecode(sourcecode, userid)
                        except Exception as ex:
                            #return "Syntax error: " + str(ex), 400
                            # TODO: Send message to user that a failure occurred.
                            print("ERROR!!!")

                        # Deserialize and get ready to execute.
                        serialized_cpu = self.redis_client.get("cpu:{0}".format(userid))
                        cpu = Cpu([], 512, 128, 0, 384)
                        cpu.deserialize_cpu(serialized_cpu)

                        # Execute.
                        counter = 0
                        try:
                            while True:
                                # Execute one step.
                                cpu.execute_step()
                                counter += 1

                                # Publish not every single step, that takes too long.
                                if counter % 10 == 0:
                                    # TODO: Output mem properly.
                                    output = cpu.get_mem()
                                    self.redis_client.publish("mem:{0}".format(userid), output)

                                    # TODO: Output console properly.
                                    output = cpu.out_stream.getvalue()
                                    self.redis_client.publish("console:{0}".format(userid), output)

                        except Exception:
                            print("Program ended. Crash?")
                            pass

                        finally:
                            pass

                        # TODO: Output console properly.
                        output = cpu.out_stream.getvalue()
                        self.redis_client.publish("console:{0}".format(userid), output)

                # Sleep for a while.
                time.sleep(0.1)

        except Exception as ex:
            # TODO: Log error here.
            print("VMWorker thread crashed: " + str(ex))

        finally:
            print("Exiting VMWorker thread.")
            exit(0)
