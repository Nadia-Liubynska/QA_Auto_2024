from modules.ui.page_objects.tumblr_sign_in_page import TumblrSignInPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TumblrBlogPage(TumblrSignInPage):
    URL = 'https://www.tumblr.com/login'
    EMAIL = 'aqa.tester.2024@gmail.com'
    PASSWORD = 'aqatester2024'

    def __init__(self):
        super().__init__()

    def go_to_blog_from_dashboard(self):
        # set up expicit wait
        wait = WebDriverWait(self.driver, 10)

        # find and click the account button
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'button[aria-label="Account"]'))
        )
        account_button = self.driver.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Account"]'
        )
        account_button.click()

        # find and click the blog button
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '.veU9u > a:nth-child(1)'))
        )
        blog_button = self.driver.find_element(
            By.CSS_SELECTOR, '.veU9u > a:nth-child(1)'
        )
        blog_button.click()

    def new_text_post(self, text, tag):
        # set up explicit wait
        wait = WebDriverWait(self.driver, 10)

        # find and click the create new post button
        wait.until(EC.presence_of_element_located((
            By.CLASS_NAME, 'ML6ef'))
        )
        new_post_button = self.driver.find_element(
            By.CLASS_NAME, 'ML6ef'
        )
        new_post_button.click()

        # find and click the new text post button
        wait.until(EC.presence_of_element_located((
            By.CLASS_NAME, 'k3o2W'))
        )
        new_text_post_button = self.driver.find_element(
            By.CLASS_NAME, 'k3o2W'
        )
        new_text_post_button.click()

        # find text box and type in it
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'p[role="document"]'))
        )
        text_box = self.driver.find_element(
            By.CSS_SELECTOR, 'p[role="document"]'
        )
        text_box.clear()
        text_box.send_keys(text)

        # add tags
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '.mbROR'))
        )
        tags_editor = self.driver.find_element(
            By.CSS_SELECTOR, '.mbROR'
        )
        tags_editor.clear()
        tags_editor.send_keys(tag)

        # find and click post button
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '.VxmZd'))
        )
        post_button = self.driver.find_element(
            By.CSS_SELECTOR, '.VxmZd'
        )
        post_button.click()

    def open_last_post(self):
        # set up explicit wait
        wait = WebDriverWait(self.driver, 10)

        # find link to the last post
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '.BSUG4'))
        )
        post_link = self.driver.find_element(
            By.CSS_SELECTOR, '.BSUG4'
        )
        post_link.click()

    def check_text(self, expected_text):
        # set up explicit wait
        wait = WebDriverWait(self.driver, 10)

        # find text of the post
        wait.until(EC.presence_of_element_located((
            By.CLASS_NAME, 'k31gt'))
        )
        text_found = self.driver.find_element(
            By.CLASS_NAME, 'k31gt'
        ).text

        return text_found == expected_text
