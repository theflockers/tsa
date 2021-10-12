import requests
import pytest

def test_sample_app_landing_page():
    try:
        req = requests.get('http://localhost:8080/sample')
        status = int(req.status_code)
        assert status == 200
    except ConnectionRefusedError as ecre:
         pytest.fail(str(ecre), pytrace=False)
    except requests.exceptions.ConnectionError as rece:
         pytest.fail(str(rece), pytrace=False)


def test_sample_app_hello_page():
    try:
        req = requests.get('http://localhost:8080/sample/hello.jsp')
        status = int(req.status_code)
        assert status == 200
    except ConnectionRefusedError as ecre:
         pytest.fail(str(ecre), pytrace=False)
    except requests.exceptions.ConnectionError as rece:
         pytest.fail(str(rece), pytrace=False)

def test_sample_app_servlet_page():
    try:
        req = requests.get('http://localhost:8080/sample/hello')
        status = int(req.status_code)
        assert status == 200
    except ConnectionRefusedError as ecre:
         pytest.fail(str(ecre), pytrace=False)
    except requests.exceptions.ConnectionError as rece:
         pytest.fail(str(rece), pytrace=False)
