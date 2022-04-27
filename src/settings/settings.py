from configparser import RawConfigParser
from pathlib import Path


def read_config() -> RawConfigParser:
    """
    read ini file and return section dict.
    """
    # path to settings.ini
    p = Path(".") / "src/settings/conf.ini"

    if not p.exists():
        raise FileNotFoundError(
            "conf.ini file not found. Does the file exist?\n"
            "If not, make one: src/settings/conf.ini.\n"
            "If the file exist, make sure the script is run from root and its spelled correctly."
        )

    config_path = p.absolute()
    # create parser which reads percent
    parser = RawConfigParser()
    # preserve case sensitive
    parser.optionxform = str
    # read file into instance
    parser.read(config_path)
    return parser


def read_section_items(section: str) -> dict:
    """
    return all items in config section
    """
    settings = read_config()
    return {param[0]: param[1] for param in settings.items(section)}
