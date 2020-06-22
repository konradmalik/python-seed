import os
import sys
import logging
import atexit
from . import demo


def configure_logging():
    level = os.environ.get("LOG_LEVEL", "debug").upper()
    logging.basicConfig(level=logging.getLevelName(level))


def cleanup():
    """Cleans up data after the application
    """
    logging.info("cleaning stuff up")


def run() -> int:
    atexit.register(cleanup)
    print("hello world!")
    print("value: {}".format(demo.get_value()))
    return 0


if __name__ == "__main__":
    configure_logging()
    logging.info("environment: %s", os.environ)
    exitcode = run()
    sys.exit(exitcode)
