import aiohttp_jinja2
from aiohttp import web
import aiohttp


class CalculatorHandler:
    def __init__(self, conf):
        self._conf = conf

    @aiohttp_jinja2.template("index.html")
    async def index(self, request):
        return {}

    @aiohttp_jinja2.template("index.html")
    async def calculate_string(self, request):
        url = self._conf["url-service"]
        result = ""
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=await request.json()) as resp:
                result = await resp.json()
                res = str(result["result"])
        return web.json_response({"result": res})
