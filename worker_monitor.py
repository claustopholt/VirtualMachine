from multiprocessing import Process
import time
import worker


def start_monitor():
    # Create a worker monitor that keeps x worker processes running.
    process_list = []

    while True:
        # Clear out dead processes.
        for process in process_list:
            if not process.is_alive():
                process_list.remove(process)

                # TODO: Log

        # Create new processes until max number is reached.
        while len(process_list) < 3:
            new_process = Process(target=worker.start_worker, args=())
            new_process.start()
            process_list.append(new_process)

            # TODO: Log

        # Sleep for a while.
        time.sleep(1)
