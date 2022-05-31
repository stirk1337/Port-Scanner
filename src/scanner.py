import socket
from queue import Queue
from threading import Thread, Lock

THREADS = 200
lock = Lock()


def port_scan(ip, port, answer):
    try:
        s = socket.socket()
        s.connect((ip, port))
        s.settimeout(0.2)
    except:
        s.close()
        with lock:
            answer.append({"port": port, "state": "close"})
    else:
        s.close()
        with lock:
            answer.append({"port": port, "state": "open"})
    finally:
        s.close()


def scan_worker(ip, q, answer):
    while True:
        port = q.get()
        port_scan(ip, port, answer)
        q.task_done()


def scanner(ip, start, end):
    answer = []
    q = Queue()
    for t in range(THREADS):
        t = Thread(target=scan_worker, args=(ip, q, answer), daemon=True)
        t.start()
    for port in range(start, end+1):
        q.put(port)
    q.join()
    return answer
