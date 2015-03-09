import socket
import sys
import mimetypes
import os
from os import getcwd
from os.path import isdir
from os.path import isfile
from os import listdir


_root = os.path.join(os.getcwd(), 'webroot')


class InvalidHTTPCodeError(Exception):
    pass


class NotGETRequestError(Exception):
    pass


class NotHTTP1_1Error(Exception):
    pass


class BadRequestError(Exception):
    pass


class ResourceNotFound(Exception):
    pass


class HttpServer(object):
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
        return "HTTP/1.1 200 OK\r\n\
        Content-Type: text/plain\r\n\r\n".encode('utf-8')

    def response_error(self, code, msg=None):
        try:
            if msg is None:
                msg = self._statusCodes[code]
            response = "HTTP/1.1 {} {}\r\n".format(code, msg)
            return response
        except KeyError:
            raise InvalidHTTPCodeError(
                u'{} is not a valid HTTP code'.format(code))

    def parse_request(self, request):
        split_list = request.split('\r\n')
        list_status = split_list[0].split(' ')
        if len(list_status) != 3:
            raise BadRequestError
        if list_status[0] != 'GET':
            raise NotGETRequestError
        if list_status[2] != 'HTTP/1.1':
            raise NotHTTP1_1Error
        return list_status[1]

    def resolve_uri(self, uri):
        u = self._root + uri
        if isdir(u):
            # return a simple HTML listing of that directorythe body.)
            body = ["<p>Directory Listing for "]
            body.append(uri)
            body.append("</p><ul>")
            dirs = []
            files = []
            for item in listdir(u):
                if isdir(u + item):
                    dirs.append(item + b'/')
                else:
                    files.append(item)
            dirs.sort()
            files.sort()
            resources = dirs + files
            for item in resources:
                body.append('<li><a href="{}">{}</a></li>'.format(item, item))
            body.append("</ul>")
            return ("".join(body), "text/html")
        elif isfile(u):
            # if the resource identified by the URI is a file, return the
            # contents of the file as the body
            # The content type value should be related to the type of file.
            with open(self._root + uri, 'rb') as resource:
                body = resource.read()
                content_type, content_encoding = mimetypes.guess_type(uri)
                return (body, content_type)
        else:
            # requested resource cannot be found, raise an appropriate # error
            raise ResourceNotFound
