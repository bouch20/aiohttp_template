from aiohttp import web
import aiohttp_autoreload
import aiohttp_jinja2
import jinja2
import asyncio
import uvloop

from handlers import BaseHandler

debug = True  # Or false

def main():
    # uvloop を用いてのasyncio高速化
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)

    app = web.Application(loop=loop)

    # templates直下をjinjaでファイル読み込み
    aiohttp_jinja2.setup(app,
        loader=jinja2.FileSystemLoader('templates/'))

    if debug:
        aiohttp_autoreload.start()
    handler = BaseHandler()
    app.add_routes([web.get('/', handler.index),
                    web.get('/answer', handler.post)])
    app.router.add_static(
        '/statics/', path='statics', name='static')
    web.run_app(app)

if __name__ == '__main__':
    main()
