import pytest
from selenium import webdriver
from PageObjects.Login_Page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGeneration


class Test_001_Login():
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGeneration.loggen()

    def test_HomePageTitle(self, setup):
        self.logger.info("test_HomePageTitle")
        self.logger.info("Verify Home Page Title")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            self.logger.info("Home Page Title Test is Passed")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\nopCommerce application\\Screenshots\\test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("Home Page Title Test is Faileed")
            assert False

    def test_login(self, setup):
        self.logger.info("Verify Login Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.Enter_Username(self.username)
        self.loginpage.Enter_Password(self.password)
        self.loginpage.Click_Login()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("Login Test is Passed")
            self.driver.close()
            assert True
        else:
            self.driver.get_screenshot_as_file("C:\\Users\\HP\\PycharmProjects\\nopCommerce application\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("Login Test is Failed")
            assert False