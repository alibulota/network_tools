from echo_server import echo_server
from echo_client import echo_client
from http1 import http1, response_ok, response_error, parse_request
from http2 import HttpServer
from http2 import ResourceNotFound
from gevent.server import StreamServer
from gevent.monkey import patch_all
from gevent.server import serve_forever


# adapted from https://github.com/gevent/gevent/blob/master/examples/echoserver.py


def handler(socket, address):
    print 'New Connection'
    buffsize = 32
    try:
        msg = ""
        finish = False
        while not finish:
            in_msg = socket.recv(buffsize)
            if in_msg:
                msg += in_msg
            else:
               socket.sendall(parse_request(msg))
               socket.close()
               finish = True
    except KeyboardInterrupt:
        socket.close()


if __name__ == '__main__':
    patch_all()
    server = StreamServer(('127.0.0.1', 50000), handler)
    print('Listening for Server')
    server.serve_forever()
