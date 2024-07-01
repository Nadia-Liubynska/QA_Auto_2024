import pytest


# api GitHub tests
@pytest.mark.api
def test_user_exists(github_api_client):
    existing_user = 'defunkt'

    user = github_api_client.get_user(existing_user)

    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api_client):
    non_existing_user = 'butenkosergii'

    user = github_api_client.get_user(non_existing_user)

    assert user['message'] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api_client):
    existing_repo = 'become-qa-auto'

    r = github_api_client.search_repo(existing_repo)

    assert r['total_count'] == 58
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api_client):
    non_existing_repo = 'sergiibutenko_repo_non_exist'

    r = github_api_client.search_repo(non_existing_repo)

    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_can_be_found(github_api_client):
    single_char = 's'

    r = github_api_client.search_repo(single_char)

    assert r['total_count'] != 0


# INDIVIDUAL ASSIGMENT

# emoji test
# check that emoji list is loaded successfully
@pytest.mark.api
@pytest.mark.emoji
def test_emoji_list(github_api_client):
    r = github_api_client.get_emoji()

    assert '2b1c.png' in r['white_large_square']


# commit list tests
# check that commit list for a valid project
# is loaded successfully
@pytest.mark.api
@pytest.mark.commit_list
def test_commit_list(github_api_client):
    existing_user = 'Nadia-Liubynska'
    existing_repo = 'QA_Auto_2024'

    r = github_api_client.get_commits(existing_user, existing_repo)

    assert r[0]['author']['type'] == 'User'
    assert r[0]['committer']['type'] == 'User'


# check that a valid error message is received if the repository has no commits
@pytest.mark.api
@pytest.mark.commit_list
def test_commit_list_empty_repo(github_api_client):
    existing_user = 'Nadia-Liubynska'
    empty_repo = 'for_test_purposes'

    r = github_api_client.get_commits(existing_user, empty_repo)

    assert r['message'] == 'Git Repository is empty.'


# check that a valid error message is displayed if the user does not exist
@pytest.mark.api
@pytest.mark.commit_list
def test_commit_list_user_doesnt_exist(github_api_client):
    non_existing_user = 'butenkosergii'
    existing_repo = 'for_test_purposes'

    r = github_api_client.get_commits(non_existing_user, existing_repo)

    assert r['message'] == 'Not Found'


# check if a valid error message is displayed if the repo does not exist
@pytest.mark.api
@pytest.mark.commit_list
def test_commit_list_repo_doesnt_exist(github_api_client):
    existing_user = 'Nadia-Liubynska'
    non_existing_repo = 'sergiibutenko_repo_non_exist'

    r = github_api_client.get_commits(existing_user, non_existing_repo)

    assert r['message'] == 'Not Found'
