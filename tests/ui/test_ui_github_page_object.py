from modules.ui.page_objects.github_sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # create an object for the Sign In Page
    sign_in_page = SignInPage()

    # go to the login page
    sign_in_page.go_to()

    # attempt to login using invalid credentials
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # assert that the login page is still displayed
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()
