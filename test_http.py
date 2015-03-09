import pytest
from echo_server import echo_server
from echo_client import echo_client
from http1 import response_ok, response_error, parse_request


def test_reponse_ok():
    response = response_ok()
    assert '200 OK' in response


def test_response_error():
    response = response_error(404, 'Page Not Found"')
    assert '404 Page Not Found' in response


def test_parse_request():
    response = parse_request('GET HTTP/1.1')
    assert '200 OK' in response
