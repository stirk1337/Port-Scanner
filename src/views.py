import json

from aiohttp import web
from src.scanner import scanner


async def ports_scanner(request):
    ip = request.match_info['ip']
    start = int(request.match_info['start'])
    end = int(request.match_info['end'])
    answer = json.dumps(scanner(ip, start, end), indent=2, sort_keys=True)
    print(answer)
    return web.json_response(answer)
