import yaml
import base64
import pathlib
from aiohttp import web
from yaml import Loader
from calculator import make_calculator

PROJ_ROOT = pathlib.Path(__file__).parent.parent


def load_config_from_yaml(filename):
    with open(filename, "r") as fd:
        data = yaml.load(fd, Loader=Loader)
    return data


def fetch_string(data):
    if data and "data" in data and len(data["data"]) > 0:
        return base64.b64decode(data["data"]).decode("utf-8")
    else:
        raise RuntimeError(str(f"arithmetic string {data} is not valid"))


async def calculate(request: web.Request) -> web.Response:
    calculate_math = make_calculator()
    try:
        data = await request.json()
        text = fetch_string(data)
        result = calculate_math(text)
        return web.json_response(
            {"result": result},
            status=200,
        )
    except TypeError as ex:
        return web.json_response(
            {"status": "fail", "reason": ex},
            status=404,
        )
    except RuntimeError as ex:
        return web.json_response(
            {"status": "fail", "reason": ex},
            status=404,
        )


app = web.Application()
app.add_routes(
    [
        web.post("/calculate", calculate),
    ]
)

if __name__ == "__main__":
    conf = load_config_from_yaml(str(f"{PROJ_ROOT}/config/config.yml"))
    host, port = conf["host"], conf["port"]
    web.run_app(app, host=host, port=port)
