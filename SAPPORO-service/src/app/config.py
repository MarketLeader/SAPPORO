# coding: utf-8
from pathlib import Path
import secrets
import os
from distutils.util import strtobool


APPLICATION_ROOT = "/"
JSON_AS_ASCII = False
JSON_SORT_KEYS = True
JSONIFY_PRETTYPRINT_REGULAR = True
LOG_FILE_PATH = "/opt/SAPPORO/SAPPORO-service/log/app/flask.log"


def generate_d_config():
    d_config = dict()
    if os.environ.get("DEBUG", None) is None:
        d_config["DEBUG"] = False
    else:
        d_config["DEBUG"] = str2bool(os.environ.get("DEBUG"))
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


def str2bool(string):
    try:
        if strtobool(string):
            return True
        else:
            return False
    except ValueError:
        raise Exception(
            "Please check your docker-compose.yml:environment, The bool value should be 'true value are y, yes, t, true, on and 1; false values are n, no, f, false, off and 0'")


def generate_secret_key():
    SECRET_KEY_FILE_NAME = "secret_key.txt"
    SECRET_KEY_FILE_PATH = Path(__file__).absolute(
    ).parent.joinpath(SECRET_KEY_FILE_NAME)
    if SECRET_KEY_FILE_PATH.exists():
        with SECRET_KEY_FILE_PATH.open(mode="w") as f:
            secret_key = secrets.token_urlsafe(32)
            f.write(secret_key)
    else:
        with SECRET_KEY_FILE_PATH.open(mode="r") as f:
            for line in f.readlines():
                if line != "":
                    secret_key = line

    return secret_key


d_config = generate_d_config()
ENABLE_GET_RUNS = str2bool(os.environ.get("ENABLE_GET_RUNS"))
ENABLE_TOKEN_AUTH = str2bool(os.environ.get("ENABLE_TOKEN_AUTH"))
LOG_LEVEL = os.environ.get("LOG_LEVEL")
