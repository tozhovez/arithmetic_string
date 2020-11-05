import base64
import yaml

from yaml import Loader

from aiohttp import web


def load_config(fname):
    with open(fname, "rt") as f:
        data = yaml.load(f, Loader=Loader)
    return data


def fetch_string(data):
    if data and "data" in data and len(data["data"]) > 0:
        return base64.b64decode(data["data"]).decode("utf-8")
    else:
        raise web.HTTPBadRequest("arithmetic string is not valid")
