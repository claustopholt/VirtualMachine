import logging
import inspect
from flask import request


# Setup logger.
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(callsite)s - %(remote_addr)s - %(path)s - %(message)s")
file_handler = logging.FileHandler("/var/log/virtualmachine.log")
file_handler.setFormatter(formatter)
_logger = logging.getLogger("VMLogger")
_logger.setLevel(logging.INFO)
_logger.addHandler(file_handler)


def log_info(message):
    log(logging.INFO, message)


def log_warning(message):
    log(logging.WARNING, message)


def log_error(message):
    log(logging.ERROR, message)


def log_critical(message):
    log(logging.CRITICAL, message)


def log(level, message):

    # Ensure remote_addr and path are set correctly if we're logging a request.
    remote_addr = ""
    path = ""
    if request:
        if "X-FORWARDED-FOR" in request.headers:
            remote_addr = request.headers["X-FORWARDED-FOR"]
        else:
            remote_addr = request.remote_addr

        path = request.path

    # Ensure "callsite" is available (two stack frames up).
    callsite_filename = str(inspect.stack()[2][1])
    callsite_filename_index = callsite_filename.rfind("/") + 1
    callsite = "{0}:{1}".format(callsite_filename[callsite_filename_index:], inspect.stack()[2][2])

    extra = {"remote_addr": remote_addr, "path": path, "callsite": callsite}

    _logger.log(level=level, msg=message, extra=extra)

