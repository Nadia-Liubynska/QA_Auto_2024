from modules.ui.page_objects.tumblr_sign_in_page import TumblrSignInPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


class TumblrBlogPage(TumblrSignInPage):

    def __init__(self):
        super().__init__()

    def go_to_blog_from_dashboard(self):
        # set up expicit wait
        wait = WebDriverWait(self.driver, 60)

        # find and click the account button
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'li[title="Account"]')))

        account_button = self.driver.find_element(
            By.CSS_SELECTOR, 'li[title="Account"]')

        account_button.click()

        # find and click the blog button
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '.wmRou[href="/blog/aqa-tester-2024"]')))

        blog_button = self.driver.find_element(
            By.CSS_SELECTOR, '.wmRou[href="/blog/aqa-tester-2024"]')

        blog_button.click()

    def new_text_post(self, text, tag):
        # set up explicit wait
        wait = WebDriverWait(self.driver, 60)

        # find and click the create new post button
        wait.until(EC.presence_of_element_located((
            By.CLASS_NAME, 'ML6ef')))

        new_post_button = self.driver.find_element(
            By.CLASS_NAME, 'ML6ef')

        new_post_button.click()

        # find and click the new text post button
        wait.until(EC.presence_of_element_located((
            By.CLASS_NAME, 'k3o2W')))

        new_text_post_button = self.driver.find_element(
            By.CLASS_NAME, 'k3o2W')

        new_text_post_button.click()

        # find the text box and type in it
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'p[role="document"]')))

        text_box = self.driver.find_element(
            By.CSS_SELECTOR, 'p[role="document"]')

        text_box.clear()
        text_box.send_keys(text)

        # add tags
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '.mbROR')))

        tags_editor = self.driver.find_element(
            By.CSS_SELECTOR, '.mbROR')

        tags_editor.clear()
        tags_editor.send_keys(tag)

        # find and click the post button
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '.VxmZd')))

        post_button = self.driver.find_element(
            By.CSS_SELECTOR, '.VxmZd')

        post_button.click()

    def open_last_post(self):
        # set up explicit wait
        wait = WebDriverWait(self.driver, 60)

        # go to the blog view
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, ".UEULa")))

        view_blog = self.driver.find_element(By.CSS_SELECTOR, ".UEULa")

        view_blog.click()

        # find and click the link to the last post
        wait.until(EC.presence_of_element_located((
            By.XPATH, "//article/header/div[2]/div/div[2]/a")))

        post_link = self.driver.find_element(
            By.XPATH, "//article/header/div[2]/div/div[2]/a")

        post_link.click()

    def delete_last_post(self):
        # set up explicit wait
        wait = WebDriverWait(self.driver, 60)

        # find and click the delete button
        wait.until(EC.presence_of_element_located((
            By.XPATH, "//article//footer/div/div[2]//button")))

        delete_button = self.driver.find_element(
            By.XPATH, "//article//footer/div/div[2]//button")

        delete_button.click()

        # find and click the Ok button
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'button[aria-label="OK"]')))

        ok_button = self.driver.find_element(
            By.CSS_SELECTOR, 'button[aria-label="OK"]')

        ok_button.click()

    def check_deletion_message(self, css_locator):
        # there are several possible messages that can be received
        # in this scenario
        message_1 = "This post went to heaven."

        message_2 = "Ghost post! Spooky. See what else is haunting "
        message_2 += f"{self.USERNAME}'s Tumblr."

        message_3 = "You're too late. This post is no more."

        message_4 = "This post isn't here anymore, but the Tumblr still is."

        message_5 = "This post is gone, gone, gone. But there's more, more, "
        message_5 += f"more, on {self.USERNAME}'s Tumblr."

        message_6 = "This post has ceased to exist."

        deletion_messages = [message_1, message_2, message_3,
                             message_4, message_5, message_6]

        # get the text of the deletion message
        found_text = self.get_text(css_locator)

        # check if the message found matches one of the possible messages
        # and return the result
        return found_text in deletion_messages

    @staticmethod
    def get_text_to_post():
        text_to_post = f"test post #{random.randint(0, 10000)}"
        return text_to_post
