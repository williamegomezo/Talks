import asyncio
import aiohttp

async def send_message():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('http://localhost:8080/ws') as ws:
            await ws.send_str('Message')

asyncio.run(send_message())
