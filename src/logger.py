import logging
import logging.handlers
import socket

logging.socket = socket
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger('main')
syslog = logging.handlers.SysLogHandler(address="/dev/log")
logger.addHandler(syslog)

