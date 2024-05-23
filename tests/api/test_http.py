import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/Nadia-Liubynska')
    print(f"Response is {r.text}")
