import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.tumblr_sign_in_page import TumblrSignInPage
from modules.ui.page_objects.tumblr_blog_page import TumblrBlogPage


# class for the api basics tests
class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Nadia"
        self.second_name = "Liubynska"

    def remove(self):
        self.name = ""
        self.second_name = ""


# fixture for the api basics tests
@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


# fixture for the GitHub part of the api tests
@pytest.fixture
def github_api_client():
    api = GitHub()
    yield api


# fixture for the database part of the api tests
@pytest.fixture
def db():
    database = Database()

    yield database

    database.delete_product_by_id(database.test_id)


# fixtures for the tumblr part of the UI tests
@pytest.fixture
def tumblr_sign_in_page():
    pageobject = TumblrSignInPage()

    yield pageobject

    pageobject.close()


@pytest.fixture
def tumblr_blog_page():
    pageobject = TumblrBlogPage()

    yield pageobject

    pageobject.close()
