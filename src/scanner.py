import socket
from threading import Thread


def port_scanner(ip, port, answer):
    s = socket.socket()
    try:
        s.settimeout(1)
        s.connect((ip, port))
        answer.append({"port": port, "status": "open"})
    except TimeoutError:
        answer.append({"port": port, "status": "close"})
    s.close()


def scanner(ip, start, end):
    threads = []
    answer = []
    for port in range(start, end + 1):
        threads.append(Thread(target=port_scanner, args=(ip, port, answer)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    answer.sort(key=lambda x: x['port'])
    return answer
