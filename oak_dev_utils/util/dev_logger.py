# Reference:
# https://alexandra-zaharia.github.io/posts/make-your-own-custom-color-formatter-with-python-logging/

import logging


class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = "\x1b[38;21m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    blue = "\x1b[38;5;33m"
    light_blue = "\x1b[38;5;45m"
    reset = "\x1b[0m"

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.light_blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset,
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


DEV_LOGGER_NAME = "dev_logger"

FORMAT = "%(message)s"

dev_logger = logging.getLogger(DEV_LOGGER_NAME)
dev_logger.setLevel(logging.DEBUG)

formatter = CustomFormatter(FORMAT)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

dev_logger.addHandler(stream_handler)
