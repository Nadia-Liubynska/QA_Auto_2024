import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # create an object for the browser control
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
        )

    # open the page https://github.com/login
    driver.get("https://github.com/login")

    # find the login field
    login_elem = driver.find_element(By.ID, "login_field")

    # enter an invalid e-mail
    login_elem.send_keys("sergiibutenko@mistakeinemal.com")

    # find the password field
    pass_elem = driver.find_element(By.ID, "password")

    # enter an invalid password
    pass_elem.send_keys("wrong password")

    # find and click the submit button
    btn_elem = driver.find_element(By.NAME, "commit")
    btn_elem.click()

    # assert that the name of the page is the same as expected
    assert driver.title == "Sign in to GitHub · GitHub"

    # close the browser
    driver.close()
