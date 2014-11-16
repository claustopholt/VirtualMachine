import logging


_logger = logging.getLogger("VMLogger")
_logger.setLevel(logging.INFO)
_logger.addHandler(logging.FileHandler("/var/log/virtualmachine.log"))


def log_info(message):
    log(logging.INFO, message)


def log(severity, message):
    _logger.log(severity, message)