import argparse
from socket import *
from datetime import datetime

MAX_BYTES = 65535

def server(port):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        data = 'Your data was {} bytes long'.format(len(data))
        text =  data.encode('ascii')
        sock.sendto(data, address)

def client(port):
    sock = socket(AF_INET, SOCK_DGRAM)
    text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))
    print('The socket for the client is {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print('The server {} replied with:  {!r}'.format(address, text))


if __name__ == "__main__":
    choices = {'client':client, 'server':server}
    parser = argparse.ArgumentParser(description = 'Send data locally via UDP')
    parser.add_argument('role', choices = choices, help='which role tp play')
    parser.add_argument('-p', metavar='PORT', type=int, default =1060, help='UDP port(default is 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)

