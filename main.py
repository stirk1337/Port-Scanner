from aiohttp import web
from src.routes import routes
from src.logger import logger


def setup():
    app = web.Application(logger=logger)
    for route in routes:
        app.router.add_route(*route)
    return app


def main():
    web.run_app(setup())


if __name__ == '__main__':
    main()