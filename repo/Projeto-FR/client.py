import socket
import signal
import sys
import datetime
import struct
import random
import time
import psutil  # not working, for some reason?


def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)


def send(cpu, mem):
    try:
        pkt = struct.pack('ff', cpu, mem)
        sock.send(pkt)
    except (socket.timeout, socket.error):
        print('Server error. Done!')
        sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##


# not the best approach, but works
ip_addr = "127.0.0.1"

tcp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip_addr, tcp_port))

order = 1

while True:
    time.sleep(3)  # wait some time

    # calc cpu utilization
    cpu = psutil.cpu_percent()

    # calc percentage of memory in use
    memory = psutil.virtual_memory()
    usedP = (memory.used * 100)/memory.total

    send(cpu, usedP)
