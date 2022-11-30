# import unittest

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
# import time
import pytest
import unittest


@pytest.mark.usefixtures("test_setup")
class TestLogin(unittest.TestCase):

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login_button()

        # driver.find_element("name", "username").send_keys("Admin")
        # driver.find_element("name", "password").send_keys("admin123")
        # driver.find_element("xpath", "//button[@type='submit']").click()
        # time.sleep(2)

    def test_logout(self):
        driver = self.driver
        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()
        x = driver.title
        assert x == "OrangeHRM"

        # driver.find_element("xpath", "//p[@class='oxd-userdropdown-name']").click()
        # driver.find_element("xpath", "//a[contains(text(),'Logout')]").click()

    if __name__ == '__main__':
        unittest.main()
