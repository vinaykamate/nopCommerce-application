import time

from PageObjects.CustomerPage import AddCustomer
from PageObjects.Login_Page import LoginPage
from PageObjects.SearchCustomer import SearchCustomer
from utilities.CustomLogger import LogGeneration
from utilities.readProperties import ReadConfig


class Test_003_SearchCustomerByEmail:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGeneration.loggen()

    def test_searchcustomerbyemail(self, setup):
        self.logger.info("********* Test_003_SearchCustomerByEmail ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.loginpage = LoginPage(self.driver)
        self.loginpage.Enter_Username(self.username)
        self.loginpage.Enter_Password(self.password)
        self.loginpage.Click_Login()
        self.logger.info("********* Login Successful ************")

        self.logger.info("********* Starting Search Customer By Email ***********")

        self.addcustomer = AddCustomer(self.driver)
        self.addcustomer.Click_Custmermenu()
        self.addcustomer.Click_Customersubmenu()

        self.searchcustomer = SearchCustomer(self.driver)
        self.searchcustomer.Enter_Email("brenda_lindgren@nopCommerce.com")
        self.searchcustomer.Click_Search()
        time.sleep(5)

        status = self.searchcustomer.SearchCustomerByEmail("brenda_lindgren@nopCommerce.com")
        assert True == status
        self.logger.info("*********** Test_003_SearchCustomerByEmail if Finished ************")
        self.driver.close()