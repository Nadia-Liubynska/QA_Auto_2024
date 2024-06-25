import pytest


# test for the sign in page
# check that user can log in using valid credentials
@pytest.mark.ui
@pytest.mark.tumblr
def test_login(tumblr_sign_in_page):
    # go to the login page
    tumblr_sign_in_page.go_to()

    # attempt to login
    tumblr_sign_in_page.try_login()

    # check if the dashboard page is loaded
    # pass the css selector of the "Home" button
    assert tumblr_sign_in_page.get_text(".ZC1wz") == "Home"


# tests for the blog page
# check that user can create a new text post
@pytest.mark.ui
@pytest.mark.tumblr
def test_create_new_post(tumblr_blog_page):
    # go to the login page
    tumblr_blog_page.go_to()

    # login into a valid account
    tumblr_blog_page.try_login()

    # go to the blog page
    tumblr_blog_page.go_to_blog_from_dashboard()

    # create and post a new text post
    test_str = tumblr_blog_page.get_text_to_post()
    test_tag = 'test_post_delete_later'
    tumblr_blog_page.new_text_post(test_str, test_tag)

    # open last post on the blog page
    tumblr_blog_page.open_last_post()

    # check that the text of the last post matches
    # the text of the newly created post
    # pass the the css selector of the text container
    assert tumblr_blog_page.get_text('.k31gt p') == test_str


# check that user can delete a post from the blog view
@pytest.mark.ui
@pytest.mark.tumblr
def test_delete_new_post(tumblr_blog_page):
    # go to the login page
    tumblr_blog_page.go_to()

    # login into a valid account
    tumblr_blog_page.try_login()

    # go to the blog page
    tumblr_blog_page.go_to_blog_from_dashboard()

    # create and post a new text post
    test_str = tumblr_blog_page.get_text_to_post()
    test_tag = 'test_post_delete_later'
    tumblr_blog_page.new_text_post(test_str, test_tag)

    # open last post on the blog page
    tumblr_blog_page.open_last_post()

    # delete last post
    tumblr_blog_page.delete_last_post()

    # check that the message about deleting a post is displayed
    assert tumblr_blog_page.check_deletion_message('.XLWxA')
