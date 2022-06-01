from aiohttp import web
from src.scanner import scanner
import socket


async def ports_scanner(request):
    ip = request.match_info['ip']
    try:
        s = socket.socket()
        s.connect((ip, 80))
        start = int(request.match_info['start'])
        end = int(request.match_info['end'])
    except socket.error:
        return web.Response(text="Invalid host.")
    except ValueError:
        return web.Response(text="Invalid port.")
    answer = scanner(ip, start, end)
    return web.json_response(answer)
