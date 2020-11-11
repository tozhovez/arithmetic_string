import asyncio
import pathlib
import yaml
import aiohttp_jinja2
import jinja2
from aiohttp import web
from yaml import Loader
from routes import setup_routes
from views import CalculatorHandler


PROJ_ROOT = pathlib.Path(__file__).parent
TEMPLATES_ROOT = pathlib.Path(__file__).parent / "templates"


def setup_jinja(app):
    loader = jinja2.FileSystemLoader(str(TEMPLATES_ROOT))
    jinja_env = aiohttp_jinja2.setup(app, loader=loader)
    return jinja_env

def load_config_from_yaml(filename):
    with open(filename, "r") as fd_reader:
        data = yaml.load(fd_reader, Loader=Loader)
    return data


async def init(loop):
    conf = load_config_from_yaml(str(f"{PROJ_ROOT}/config/config.yml"))
    app = web.Application()
    setup_jinja(app)
    handler = CalculatorHandler(conf)
    setup_routes(app, handler, PROJ_ROOT)
    host, port = conf["host"], conf["port"]
    return app, host, port


def main():
    loop = asyncio.get_event_loop()
    app, host, port = loop.run_until_complete(init(loop))
    web.run_app(app, host=host, port=port)


if __name__ == "__main__":
    main()
