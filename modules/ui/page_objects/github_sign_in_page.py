from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # find the login field
        login_elem = self.driver.find_element(By.ID, "login_field")

        # enter an invalid username
        login_elem.send_keys(username)

        # find the password field
        pass_elem = self.driver.find_element(By.ID, "password")

        # enter an invalid password
        pass_elem.send_keys(password)

        # find and click the submit button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
