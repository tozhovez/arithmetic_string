import aiohttp
import asyncio
import base64
import json
import pathlib


async def main():
    url = "http://127.0.0.1:50772/calculate"
    string_data = "5+5-(8+4)*5"
    d = string_data.encode("UTF-8")
    b = base64.b64encode(d).decode("UTF-8")
    print(string_data)
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"data": b}) as resp:
            print(await resp.text())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
