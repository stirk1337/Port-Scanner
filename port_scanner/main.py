from aiohttp import web
from src.routes import routes


def get_app():
    app = web.Application()
    for route in routes:
        app.router.add_route(*route)
    return app


if __name__ == "__main__":
    web.run_app(get_app())
