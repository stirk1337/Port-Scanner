from socket import socket
from threading import Thread

answer = []


def port_scanner(ip, port):
    s = socket()
    status = 'close'
    try:
        s.settimeout(1)
        s.connect((ip, port))
        status = 'open'
    except:
        pass
    answer.append({"port": port, "status": status})


def scanner(ip, start, end):
    answer.clear()
    for port in range(start, end + 1):
        t = Thread(target=port_scanner, args=(ip, port))
        t.start()
    return answer
