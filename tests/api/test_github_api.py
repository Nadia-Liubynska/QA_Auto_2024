import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user('butenkosergii')
    assert user['message'] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_can_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
@pytest.mark.emoji
def test_emoji_list(github_api):
    r = github_api.get_emoji()
    assert '2b1c.png' in r['white_large_square']


@pytest.mark.api
@pytest.mark.commit_list
def test_commit_list(github_api):
    r = github_api.get_commits('Nadia-Liubynska', 'QA_Auto_2024')
    assert r[0]['author']['type'] == 'User'
    assert r[0]['committer']['type'] == 'User'


@pytest.mark.api
@pytest.mark.commit_list
def test_commit_list_empty_repo(github_api):
    r = github_api.get_commits('Nadia-Liubynska', 'for_test_purposes')
    assert r['message'] == 'Git Repository is empty.'


@pytest.mark.api
@pytest.mark.commit_list
def test_commit_list_user_doesnt_exist(github_api):
    r = github_api.get_commits('butenkosergii', 'for_test_purposes')
    assert r['message'] == 'Not Found'


@pytest.mark.api
@pytest.mark.commit_list
def test_commit_list_repo_doesnt_exist(github_api):
    r = github_api.get_commits('Nadia-Liubynska',
                               'sergiibutenko_repo_non_exist')
    assert r['message'] == 'Not Found'
