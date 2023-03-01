import time

from PageObjects.CustomerPage import AddCustomer
from PageObjects.Login_Page import LoginPage
from PageObjects.SearchCustomer import SearchCustomer
from utilities.CustomLogger import LogGeneration
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGeneration.loggen()

    def test_searchcustomerbyname(self, setup):
        self.logger.info("********* Test_004_SearchCustomerByEmail ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.loginpage = LoginPage(self.driver)
        self.loginpage.Enter_Username(self.username)
        self.loginpage.Enter_Password(self.password)
        self.loginpage.Click_Login()
        self.logger.info("********* Login Successful ************")

        self.logger.info("********* Starting Search Customer By Name ***********")

        self.addcustomer = AddCustomer(self.driver)
        self.addcustomer.Click_Custmermenu()
        self.addcustomer.Click_Customersubmenu()

        self.searchcustomer = SearchCustomer(self.driver)
        self.searchcustomer.Enter_FName("Virat")
        self.searchcustomer.Enter_LName("Kohli")
        self.searchcustomer.Click_Search()
        time.sleep(5)

        status = self.searchcustomer.SearchCustomerByName("Virat Kohli")
        assert True == status
        self.logger.info("*********** Test_003_SearchCustomerByName if Finished ************")
        self.driver.close()
