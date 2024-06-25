import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.tumblr_sign_in_page import TumblrSignInPage
from modules.ui.page_objects.tumblr_blog_page import TumblrBlogPage


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


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def db():
    database = Database()

    yield database

    database.delete_product_by_id(999)


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
