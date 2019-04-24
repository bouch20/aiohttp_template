from aiohttp import web
from handlers import BaseHandler
import aiohttp_jinja2
import jinja2

def main():
    app = web.Application()
    aiohttp_jinja2.setup(app,
        loader=jinja2.FileSystemLoader('templates/'))
    handler = BaseHandler()
    app.add_routes([web.get('/', handler.index),
                    web.get('/answer', handler.post)])
    app.router.add_static(
        '/statics/', path='statics', name='static')
    web.run_app(app)

if __name__ == '__main__':
    main()
