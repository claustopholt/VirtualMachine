import os
import time


def start_worker():
    # See if there is work to be done.
    try:
        counter = 0
        pid = os.getpid()
        while True:
            counter += 1
            if counter > 5:
                raise "blah"

            #print("Worker {0}, counter {1}".format(pid, counter))

            # Sleep for a while.
            time.sleep(1)

    except:
        # Log error here.
        pass

    finally:
        exit(0)

