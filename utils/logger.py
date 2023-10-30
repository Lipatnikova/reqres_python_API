import logging
import logging.handlers
import os

path = os.path.join(os.path.dirname(__file__), '..', 'utils', 'logs', 'logger.log')


def setup_logging(name):
    logger = logging.getLogger(name)
    msg_format = '%(asctime)s %(name)s %(levelname)s %(message)s'
    logger.setLevel(logging.DEBUG)
    file_handler = logging.handlers.RotatingFileHandler(path, mode="a", maxBytes=2048, backupCount=10,
                                                        encoding=None, delay=False, errors=None)
    file_handler.setFormatter(logging.Formatter(msg_format))
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)


setup_logging("reqres_python_API")
