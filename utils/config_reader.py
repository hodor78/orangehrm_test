from pathlib import Path
import configparser

# Construct the path to the config.ini file dynamically
config_path = Path(__file__).parent.parent / "config.ini"

# Function to read configuration values from config.ini
def read_config():
    config = configparser.ConfigParser()
    config.read(config_path)
    return config