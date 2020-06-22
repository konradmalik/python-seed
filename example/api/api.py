from flask import jsonify, Blueprint, current_app

from .. import config

api1 = Blueprint('api_v1', __name__, url_prefix="/api/v1")

def get_value() -> str:
    conf = config.get_section("demo")
    return conf['demo']

@api1.route('/hello', methods=['GET'])
def hello():
    current_app.logger.info("hello received")
    return jsonify(get_value())
