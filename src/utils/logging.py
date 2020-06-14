import logging
from logging.handlers import RotatingFileHandler


def setup_logging(filename: str = None):
    formatter = logging.Formatter("[%(asctime)s] %(module)s %(levelname)s %(message)s")
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(logging.StreamHandler())
    if filename:
        root.addHandler(RotatingFileHandler(filename, maxBytes=100000))
    for handler in root.handlers:
        handler.setFormatter(formatter)
