from modules.ui.page_objects.tumblr_sign_in_page import TumblrSignInPage
from modules.ui.page_objects.tumblr_blog_page import TumblrBlogPage
import pytest


@pytest.mark.ui
@pytest.mark.tumblr
def test_login():
    sign_in_page = TumblrSignInPage()

    sign_in_page.go_to()

    sign_in_page.try_login()

    assert sign_in_page.check_title("Register - Login") is False

    sign_in_page.close()


@pytest.mark.ui
@pytest.mark.tumblr
def test_new_post():
    tumblr_blog_page = TumblrBlogPage()

    tumblr_blog_page.go_to()

    tumblr_blog_page.try_login()

    tumblr_blog_page.go_to_blog_from_dashboard()

    test_str = 'test post'
    test_tag = 'test_post_delete_later'
    tumblr_blog_page.new_text_post(test_str, test_tag)

    tumblr_blog_page.open_last_post()

    assert tumblr_blog_page.check_text('test post')

    tumblr_blog_page.close()
