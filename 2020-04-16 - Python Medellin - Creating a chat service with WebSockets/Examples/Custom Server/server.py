import asyncio
import logging
import websockets

logging.basicConfig(level=logging.INFO)

class Server:
    clients = set()

    def register(self, websocket: websockets.WebSocketServerProtocol) -> None:
        self.clients.add(websocket)
        logging.info(f'{websocket.remote_address} connects.')

    def unregister(self, websocket: websockets.WebSocketServerProtocol) -> None:
        self.clients.remove(websocket)
        logging.info(f'{websocket.remote_address} disconnects.')

    async def send_to_clients(self, message: str, websocket: websockets.WebSocketServerProtocol) -> None:
        if self.clients:
            await asyncio.gather(*[client.send(message) for client in self.clients])

    async def ws_handler(self, websocket: websockets.WebSocketServerProtocol, uri: str) -> None:
        self.register(websocket)
        try:
            await self.distribute(websocket)
        finally:
            self.unregister(websocket)

    async def distribute(self, websocket: websockets.WebSocketServerProtocol) -> None:
        async for message in websocket:
            await self.send_to_clients(message, websocket)


if __name__ == '__main__':
    server = Server()
    start_server = websockets.serve(server.ws_handler, 'localhost', 4000)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.run_forever()