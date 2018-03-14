import aiohttp
import asyncio
import async_timeout
import json

async def main():
    url = 'http://127.0.0.1:5000'
    async with aiohttp.ClientSession() as session:
        async with async_timeout.timeout(10):
            async with session.post(
                url,
                data=json.dumps({"name": "Mogka BODY"}),
                # must set content type header to be json
                # for flask to use get_json
                headers={
                    "Content-Type": "application/json", 
                    "name": "Mogka HEADER"},
            ) as response:
                print(await response.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
