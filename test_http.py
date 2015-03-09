import pytest
from echo_server import echo_server
from echo_client import echo_client
from http1 import http1, response_ok, response_error, parse_request
from http2 import HttpServer
from http2 import ResourceNotFound


def test_reponse_ok():
    response = '200 OK'
    content_type = 'text/plain'
    actual = http1.response_ok()
    assert response in actual
    assert content_type in actual


def test_response_error():
    response = response_error(404, 'Page Not Found"')
    assert '404 Page Not Found' in response


def test_parse_request():
    response = parse_request('GET HTTP/1.1')
    assert '200 OK' in response


def test_resolve_uri():
    test_str = u'Hey, it is Bob.'
    server = HttpServer()
    body, content_type = server.resolve_uri(b"sample.text")
    assert content_type == b"text/html"
    assert body.decode('utf-8') == test_str


def assert_resolve_uri_error():
    server = HttpServer()
    with pytest.raises(ResourceNotFound):
        server.resolve_uri(b"blahdblahnah.text")


def test_resolve_uri_content_type():
    server = HttpServer()
    body, content_type = server.resolve_uri(b"")
    assert content_type == b"text/html"
