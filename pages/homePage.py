class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.userdropdown_name_xpath = "//p[@class='oxd-userdropdown-name']"
        self.logout_link = "//a[contains(text(),'Logout')]"

    def click_welcome(self):
        self.driver.find_element("xpath", self.userdropdown_name_xpath).click()

    def click_logout(self):
        self.driver.find_element("xpath", self.logout_link).click()
