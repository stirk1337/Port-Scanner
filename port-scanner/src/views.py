from aiohttp import web
from src.scanner import scanner
from src.logger import log
import socket
import syslog


async def ports_scanner(request):
    log(syslog.LOG_INFO, request)
    ip = request.match_info['ip']
    try:
        s = socket.socket()
        s.connect((ip, 80))
        start = int(request.match_info['start'])
        end = int(request.match_info['end'])
    except socket.error:
        log(syslog.LOG_ERR, request)
        return web.Response(text="Invalid host.")
    except ValueError:
        log(syslog.LOG_ERR, request)
        return web.Response(text="Invalid port.")
    finally:
        s.close()
    answer = scanner(ip, start, end)
    return web.json_response(answer)

