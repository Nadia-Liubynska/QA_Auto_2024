import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_does_not_exist(github_api):
    user = github_api.get_user('butenkosergii')
    assert user['message'] == "Not Found"
