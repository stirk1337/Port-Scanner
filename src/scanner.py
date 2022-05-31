import socket
from queue import Queue
from threading import Thread

q = Queue()
THREADS = 200
answer = []


def port_scan(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, port))
        s.settimeout(0.2)
    except:
        answer.append({'port': port, 'state': 'close'})
    else:
        answer.append({'port': port, 'state': 'open'})
    finally:
        s.close()


def scan_worker(ip):
    global q
    while True:
        port = q.get()
        port_scan(ip, port)
        q.task_done()


def scanner(ip, start, end):
    global answer
    answer = []
    for t in range(THREADS):
        t = Thread(target=scan_worker, args=(ip,), daemon=True)
        t.start()
    for port in range(start, end+1):
        q.put(port)
    q.join()
    return answer
