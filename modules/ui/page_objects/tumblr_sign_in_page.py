from modules.ui.page_objects.base_page import BasePage
from config.credentials import Tumblr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TumblrSignInPage(BasePage, Tumblr):
    URL = 'https://www.tumblr.com/login'

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(TumblrSignInPage.URL)

    def try_login(self):
        # set up expicit wait
        wait = WebDriverWait(self.driver, 30)

        # find the e-mail field
        wait.until(EC.presence_of_element_located((
            By.NAME, 'email')))
        login_field = self.driver.find_element(By.NAME, 'email')

        # enter a valid e-mail
        login_field.send_keys(TumblrSignInPage.EMAIL)

        # find the password field
        password_field = self.driver.find_element(By.NAME, 'password')

        # enter valid password
        password_field.send_keys(TumblrSignInPage.PASSWORD)

        # find the login button
        login_button = self.driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]')

        # click the login button
        login_button.click()

    def get_text(self, css_locator):
        # set up explicit wait
        wait = WebDriverWait(self.driver, 30)

        # find where the text is using css locator
        # passed to the method
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, css_locator)))

        found_text = self.driver.find_element(
            By.CSS_SELECTOR, css_locator).text

        return found_text
