from multiprocessing import Process
from signal import *
import time
import os
import sys
import subprocess
import VMWorker


# Create a worker monitor that keeps x worker processes running.
process_list = []
keep_going = True

def start_monitor():
    global process_list
    global keep_going
    while keep_going:
        # Clear out dead processes.
        for process in process_list:
            if not process.is_alive():
                process_list.remove(process)

        # Create new processes until max number is reached.
        while len(process_list) < 3:
            worker_obj = VMWorker.VMWorker()
            new_process = Process(target=worker_obj.start_worker, args=(), name="Worker{0}".format(len(process_list)))
            new_process.start()
            process_list.append(new_process)

        # Sleep for a while.
        time.sleep(1)

    #sys.stderr.write("Terminating all subprocesses.")
    #pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    #os.killpg(pro.pid, signal.SIGTERM)

    #for proc in process_list:
        #sys.stderr.write("Terminating process {0}\r\n".format(proc.pid))
        #proc.terminate()


def signal_handler(signal_type, frame):
    global keep_going
    keep_going = False


if __name__ == "__main__":
    # This module is started up as a process either manually or by Supervisor.
    for sig in (SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM):
        signal(SIGTERM, signal_handler)

    start_monitor()