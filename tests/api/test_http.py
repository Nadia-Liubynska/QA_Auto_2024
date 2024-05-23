import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/Nadia-Liubynska')
    print(f"Response Body is {r.json()}")
    print(f"Response Status code is {r.status_code}")
    print(f"Response Headers is {r.headers}")
