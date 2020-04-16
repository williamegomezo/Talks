import asyncio
import websockets

async def send(message: str, host: str, port: int) -> None:
    websocket_resource_url = f'ws://{host}:{port}'
    async with websockets.connect(websocket_resource_url) as websocket:
        await websocket.send(message)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send(message='Sender', host='localhost', port=4000))