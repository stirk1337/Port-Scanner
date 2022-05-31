import json

from aiohttp import web
from src.scanner import scanner


async def ports_scanner(request):
    ip = request.match_info['ip']
    start = int(request.match_info['start'])
    end = int(request.match_info['end'])
    answer = scanner(ip, start, end)
    return web.json_response(answer)
