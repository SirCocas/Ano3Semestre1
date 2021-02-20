import socket
import threading
import signal
import sys
import struct


def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##


def handle_client_connection(client_socket, address):
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    try:
        while True:
            # information is received and parsed into usable variables
            information = client_socket.recv(struct.calcsize('ff'))
            cpu, mem = struct.unpack('ff', information)

            # information is printed (could be a separate function)
            print('From ' + str(address))
            print('CPU utilization: ' + str(cpu))
            print('Percentage of memory in use: ' + str(mem))
            print('---------------------')

    except (socket.timeout, socket.error):
        print('Client {} error. Done!'.format(address))


ip_addr = "0.0.0.0"
tcp_port = 5005

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_addr, tcp_port))
server.listen(5)  # max backlog of connections

print('Listening on {}:{}'.format(ip_addr, tcp_port))

while True:
    client_sock, address = server.accept()
    client_handler = threading.Thread(
        target=handle_client_connection, args=(client_sock, address), daemon=True)
    client_handler.start()