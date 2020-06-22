import os
from configparser import SafeConfigParser

class CaseConfigParser(SafeConfigParser):
    """Avoid infinite loop when using uppercase configs from Env.
    Explanation: The problem here is with optionxform, which turns all options to lower case by default.
    Eventually, it will have key and value equal.
    """
    def optionxform(self, optionstr):
        return optionstr

def read(*filenames) -> CaseConfigParser:
    """Reads the specified file as config

    Arguments:
        filenames -- files to read

    Returns:
        configparser.ConfigParser -- parsed config
    """
    config = CaseConfigParser(os.environ)
    config.read(filenames)
    return config

def get_section(section: str):
    """Gets a speficied section from the config file

    Arguments:
        section {str} -- section to get from the file

    Returns:
        Section from the config file
    """
    try:
        sec = read("local.ini", "overrides.ini")[section]
    except:
        sec = read("local.ini")[section]
    return sec

