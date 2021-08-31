from aiohttp import web, WSMsgType

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    async for msg in ws:
        print(msg)
    return ws


app = web.Application()
app.router.add_get('/ws', websocket_handler)
web.run_app(app)
