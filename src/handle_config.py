import os
from dotenv import find_dotenv, load_dotenv

from config import params

load_dotenv(find_dotenv())

config = {"API_KEY": None, "USER_ID": None}

for element in config:
    try:
        config[f"{element}"] = os.getenv(f"{element}")
    except TypeError:
        config[f"{element}"] = params[f"{element}"]
    finally:
        if config[f"{element}"] is None:
            print(
                "ERROR: Lack of correct variable in environment variables, or config.py"
            )

print(config)

"""
load_dotenv(find_dotenv())

if dotenv_exists is True:
    API_KEY = os.getenv("API_KEY")
    USER_ID = os.getenv("USER_ID")
"""
