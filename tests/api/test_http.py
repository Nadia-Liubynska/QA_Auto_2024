import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')

    print(f"Response is {r.text}")


@pytest.mark.http
def test_second_request():
    existing_user = 'defunkt'

    r = requests.get(f'https://api.github.com/users/{existing_user}')
    body = r.json()
    headers = r.headers

    assert body['name'] == "Chris Wanstrath"
    assert r.status_code == 200
    assert headers['Server'] == "istio-envoy"


@pytest.mark.http
def test_status_code_request():
    non_existing_user = 'sergii_butenko'

    r = requests.get(f'https://api.github.com/users/{non_existing_user}')

    assert r.status_code == 404
