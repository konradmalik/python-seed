import logging
import atexit
import os

from flask import Flask

from . import api
from .. import config

def configure_logging():
    try:
        logging.config.dictConfig({
            'version': 1,
            'formatters': {'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }},
            'handlers': {'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            }},
            'root': {
                'level': os.environ.get("LOG_LEVEL", "debug").upper(),
                'handlers': ['wsgi']
            }
        })
    except:
        # this is ok, should work in production
        # but throw exceptions in dev, but in dev we see debug logs either way
        pass

def _cleanup():
    """Cleans-up after the application
    """
    logging.info("cleaning stuff up")


def create_app():
    """Creates the application
    """
    configure_logging()
    ap = Flask(__name__)
    ap.register_blueprint(api.api1)
    atexit.register(_cleanup)
    return ap


app = create_app()


if __name__ == "__main__":
    logging.info("environment: %s", os.environ)
    conf = config.get_section('server')
    host = conf.get('host')
    port = conf.get('port')
    debug = conf.getboolean('debug')
    app.run(host=host, port=port, debug=debug, use_reloader=True)
