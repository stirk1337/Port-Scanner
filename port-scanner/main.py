from aiohttp import web
from src.routes import routes
from src.app import get_app

if __name__ == "__main__":
    web.run_app(get_app())
