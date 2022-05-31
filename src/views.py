import aiohttp

async def port_scanner(request):
    return aiohttp.web.json_response(({'status': 'OK'}))