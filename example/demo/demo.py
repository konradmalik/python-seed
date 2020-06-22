from .. import config

def get_value():
    conf = config.get_section("demo")
    return conf['demo']
