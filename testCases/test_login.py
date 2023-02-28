import time

import pytest
from selenium import webdriver
from PageObjects.Login_Page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGeneration
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getapplicationURL()
    path = "C:\\Users\\HP\\PycharmProjects\\nopCommerce application\\TestData\\LoginData.xlsx"
    logger = LogGeneration.loggen()

    def test_login(self, setup):
        self.logger.info("Verify Login Test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        print("Number of Rows is a Excel:",self.rows)
        lst_status = []

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp_result = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.loginpage.Enter_Username(self.user)
            self.loginpage.Enter_Password(self.password)
            self.loginpage.Click_Login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp_result == "Pass":
                    self.logger.info("******Passed*******")
                    self.loginpage.Click_Logout()
                    lst_status.append("Pass")
                elif self.exp_result == "Fail":
                    self.logger.info("******Failed*******")
                    self.loginpage.Click_Logout()
                    lst_status.append("Fail")
            if act_title != exp_title:
                if self.exp_result == "Pass":
                    self.logger.info("******Failed*******")
                    lst_status.append("Fail")
                elif self.exp_result == "Fail":
                    self.logger.info("******Passed*******")
                    lst_status.append("Pass")
                    
        if "Fail" not in lst_status:
            self.logger.info("*****Login DDT test passed****")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****Login DDT test failed*****")
            self.driver.close()
            assert False

        self.logger.info("*****End of Login DDT Test*****")
        self.logger.info("*****Completed TC_LoginDDT_002*****")