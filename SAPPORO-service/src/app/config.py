# coding: utf-8
from pathlib import Path
import secrets
import os
from distutils.util import strtobool


APPLICATION_ROOT = "/"
JSON_AS_ASCII = False
JSON_SORT_KEYS = True
JSONIFY_PRETTYPRINT_REGULAR = True
LOG_FILE_PATH = Path("/opt/SAPPORO/SAPPORO-service/log/app/flask.log")
LOG_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)


def str2bool(arg):
    if isinstance(arg, str):
        try:
            if strtobool(arg):
                return True
            else:
                return False
        except ValueError:
            raise Exception(
                "Please check your docker-compose.yml:environment, "
                "The bool value should be 'true value are y, yes, t, "
                "true, on and 1; false values are n, no, f, false, off and 0'")
    else:
        if arg:
            return True
        else:
            return False


def generate_secret_key():
    SECRET_KEY_FILE_NAME = "secret_key.txt"
    SECRET_KEY_FILE_PATH = Path(__file__).absolute(
    ).parent.joinpath(SECRET_KEY_FILE_NAME)
    if SECRET_KEY_FILE_PATH.exists():
        with SECRET_KEY_FILE_PATH.open(mode="r") as f:
            for line in f.readlines():
                if line != "":
                    secret_key = line
    else:
        with SECRET_KEY_FILE_PATH.open(mode="w") as f:
            secret_key = secrets.token_urlsafe(32)
            f.write(secret_key)

    return secret_key


def generate_d_config():
    d_config = dict()
    d_config["DEBUG"] = str2bool(os.environ.get("DEBUG", True))
    if d_config["DEBUG"]:
        d_config["ENV"] = "development"
        d_config["TESTING"] = True
    else:
        d_config["ENV"] = "production"
        d_config["TESTING"] = False
    d_config["APPLICATION_ROOT"] = APPLICATION_ROOT
    d_config["JSON_AS_ASCII"] = JSON_AS_ASCII
    d_config["JSON_SORT_KEYS"] = JSON_SORT_KEYS
    d_config["JSONIFY_PRETTYPRINT_REGULAR"] = JSONIFY_PRETTYPRINT_REGULAR
    d_config["SECRET_KEY"] = generate_secret_key()

    return d_config


d_config = generate_d_config()
ENABLE_GET_RUNS = str2bool(os.environ.get("ENABLE_GET_RUNS", False))
ENABLE_TOKEN_AUTH = str2bool(os.environ.get("ENABLE_TOKEN_AUTH", False))
LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")
