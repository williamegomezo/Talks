from aiohttp import web
from aiohttp.web_middlewares import middleware


async def saved(request):
    data = request.app['data']
    return web.Response(text=data)


async def hello(request):
    return web.Response(text="Hello, world")


@middleware
async def mini_middleware(request, handler):
    resp = await handler(request)
    print('mini_middleware', resp.text)
    return resp

async def create_app():
    app = web.Application(middlewares=[mini_middleware])
    app['data'] = 'Saved data'
    app.add_routes([web.get('/', hello), web.get('/saved', saved)])
    return app

if __name__ == '__main__':
    web.run_app(create_app())
