import os
from dotenv import find_dotenv, load_dotenv

from config import params

load_dotenv(find_dotenv())

config = {"API_KEY": None, "USER_ID": None, "SEARCH_INFO_LOCATION": None}

for element in config:
    try:
        config[f"{element}"] = os.getenv(f"{element}")
    except TypeError:
        config[f"{element}"] = params[f"{element}"]
    finally:
        if config[f"{element}"] is None and params[f"{element}"] is not None:
            config[f"{element}"] = params[f"{element}"]

        if config[f"{element}"] is None:
            print("Something went wrong when importing config")


print(config)

"""
load_dotenv(find_dotenv())

if dotenv_exists is True:
    API_KEY = os.getenv("API_KEY")
    USER_ID = os.getenv("USER_ID")
"""
