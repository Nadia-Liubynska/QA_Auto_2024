from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class TumblrSignInPage(BasePage):
    URL = 'https://www.tumblr.com/login'
    EMAIL = 'aqa.tester.2024@gmail.com'
    PASSWORD = 'aqatester2024'

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(TumblrSignInPage.URL)

    def try_login(self):
        # find e-mail field
        login_field = self.driver.find_element(By.NAME, 'email')

        # enter valid e-mail
        login_field.send_keys(TumblrSignInPage.EMAIL)

        # find password field
        password_field = self.driver.find_element(By.NAME, 'password')

        # enter valid password
        password_field.send_keys(TumblrSignInPage.PASSWORD)

        # find login button
        login_button = self.driver.find_element(By.CSS_SELECTOR,
                                                'button[type="submit"]')

        # click login button
        login_button.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
