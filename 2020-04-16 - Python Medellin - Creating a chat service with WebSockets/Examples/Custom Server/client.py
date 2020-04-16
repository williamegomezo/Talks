import asyncio
import aioconsole
import logging
import websockets

logging.basicConfig(level=logging.INFO)


async def send_messages(websocket: websockets.WebSocketClientProtocol):
    stdin, _ = await aioconsole.get_standard_streams()
    async for line in stdin:
        await websocket.send(line.decode())

async def receive_messages(websocket: websockets.WebSocketClientProtocol):
    async for message in websocket:
        log_message(message)

async def client_handler(websocket: websockets.WebSocketClientProtocol) -> None:
    while True:
        await asyncio.gather(*[receive_messages(websocket), send_messages(websocket)])

async def connect(host: str, port: int) -> None:
    websocket_resource_url = f'ws://{host}:{port}'
    async with websockets.connect(websocket_resource_url) as websocket:
        await client_handler(websocket)

def log_message(message: str) -> None:
    logging.info(f'Message: {message}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect(host='localhost', port=4000))