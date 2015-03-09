import socket
import sys


class HttpServer(Exception):
    def http_server():
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


    def response_ok():


    def response_error(self, code, msg=None):
        try:
            if msg is None:
                msg = self._statusCodes[code]
            response = "HTTP/1.1 {} {}\r\n".format(code, msg)
            return response
        except KeyError:
            raise InvalidHttpCodeError(
                u'{} is not a valid HTTP code'.format(code))


    def parse_request(self, request):
        split_list = request.split('\r\n')
        list_status = list_[0].split(' ')
        if len(list_status) != 3:
            raise BadRequestError
        if list_status[0] != 'GET':
            raise NotGETRequestError
        if list_status[2] != 'HTTP/1.1':
            raise NotHTTP1_1Error
        reutrn list_status[1]

if __name__ == '__main__':
    echo_server()
