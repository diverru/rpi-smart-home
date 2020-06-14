#!/usr/bin/env python3

import logging

from rpi.hardware import get_temperature
from utils.env import Env
from utils.graphite import Graphite
from utils.logging import setup_logging


def main():
    setup_logging(Env.RPI_LOG_FILE.resolve())
    try:
        logging.info(f"Starting")
        with Graphite() as graphite:
            graphite.send("home.heartbeat", 1)
            graphite.send_gauge("home.cpu_temperature", get_temperature())
        logging.info(f"Done")
    except:
        logging.exception("")
        raise


if __name__ == "__main__":
    main()
