import aiohttp_jinja2
from aiohttp import web
from calculate.calculator import make_calculator

from calculate.utils import fetch_string


class CalculatorHandler:
    def __init__(self, conf):
        self._conf = conf

    @aiohttp_jinja2.template("index.html")
    async def index(self, request):
        return {}

    @aiohttp_jinja2.template("timeline.html")
    async def calculate(self, request):
        data = await request.json()
        string_data = fetch_string(data)
        calc = make_calculator()
        res = calc(string_data)
        return web.json_response({"result": res})
