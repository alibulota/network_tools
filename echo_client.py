import socket
import sys


def echo_client(msg):
    user_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)
    user_socket.connect(('127.0.01', 50000))
    if type(msg) == unicode:
        msg = msg.encode('utf-8')
    user_socket.sendall(msg)
    user_socket.shutdown(socket.SHUT_WR)
    message = ''

    while True:
        msg_recieved = user_socket.recv(32)
        message += msg_recieved
        if len(msg_recieved) < 32:
            print msg_recieved
            break
    user_socket.close()
    return unicode(message, 'utf-8')

if __name__ == "__main__":
    echo_client(sys.argv[1])
