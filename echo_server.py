import socket
import sys

def echo_server():
    user_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)
    user_socket.bind(('127.0.0.1', 50000))
    user_socket.listen(1)

    while True:
        conn, addr = user_socket.accept()
        message = ''

        while True:
            msg_recieved = conn.recv(32)
            message += msg_recieved
            if len(msg_recieved) < 32:
                break
        try:
            # This seems to be a mac-specific bug
            conn.shutdown(socket.SHUT_RD)
        except Exception, e:
            pass
        print message
        conn.sendall(message)
        conn.shutdown(socket.SHUT_WR)
        conn.close()
        if message == "quit":
            break
    user_socket.close()
    return unicode(message, 'utf=8')


if __name__ == '__main__':
    echo_server()
