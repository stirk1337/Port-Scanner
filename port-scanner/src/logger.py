import syslog


def log(level, request):
    syslog.syslog(level, f'{level} {request.method} {request.path} {request.remote}')
