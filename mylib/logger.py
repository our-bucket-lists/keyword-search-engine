import logging

class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'
    header = '[%(asctime)s][%(levelname)8s][%(module)14s] '
    msg = '%(message)s'

    def __init__(self):
        super().__init__()
        self.FORMATS = {
            logging.DEBUG: self.grey + self.header + self.reset + self.msg,
            logging.INFO: self.blue + self.header + self.reset + self.msg,
            logging.WARNING: self.yellow + self.header + self.msg + self.reset,
            logging.ERROR: self.red + self.header + self.msg + self.reset,
            logging.CRITICAL: self.bold_red + self.header + self.msg + self.reset,
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def init_root_logger(level=logging.DEBUG):
    # Clean up all handlers
    logging.getLogger().handlers.clear()

    # Create stdout handler for logging to the console (logs all five levels)
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(CustomFormatter())

    # Add the stram handler to the root logger
    logging.getLogger().addHandler(stdout_handler)
    logging.getLogger().setLevel(level)
