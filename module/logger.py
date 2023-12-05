import logging
import time
from datetime import datetime
import os

LOGGING_FORMAT = '%(asctime)s [%(levelname)s]: %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT, datefmt=DATE_FORMAT)

# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# time.sleep(10)

# ref: https://www.codemotion.com/magazine/ai-ml/big-data/logging-in-python-a-broad-gentle-introduction/
def logger_config(filename='log'):
    log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    global logFile
    local_path = 'log/' +filename + '.log'
    logFile = os.path.join(os.path.dirname(os.path.realpath(__file__)), local_path)

    global file_handler
    file_handler = logging.FileHandler(logFile)
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    stream_handler.setLevel(logging.DEBUG)

    # Get the root logger
    global app_log
    app_log = logging.getLogger('myLog')
    app_log.setLevel(logging.DEBUG)

    # Add both Handlers
    app_log.addHandler(file_handler)
    app_log.addHandler(stream_handler)

    return app_log


if __name__ == '__main__':

    # TODO: On Start
    now = f"{datetime.now():%Y-%m-%d_%H%M%S}"
    logger_config(now)

    # Main program
    app_log.info('Testing info')
    time.sleep(10)

    # TODO: On End
    # Close the handlers
    file_handler.close()
    # os.remove(logFile)