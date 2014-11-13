from multiprocessing import Process
import time
import VMWorker


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
            worker_obj = VMWorker.VMWorker()
            new_process = Process(target=worker_obj.start_worker, args=())
            new_process.start()
            process_list.append(new_process)

            # TODO: Log

        # Sleep for a while.
        time.sleep(1)


if __name__ == "__main__":

    start_monitor()