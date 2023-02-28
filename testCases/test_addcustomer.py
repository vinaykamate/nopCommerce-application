import random
import string

from selenium.webdriver.common.by import By

from PageObjects.CustomerPage import AddCustomer
from PageObjects.Login_Page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGeneration


class Test_003_AddCustomer:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGeneration.loggen()

    def test_addcustomer(self, setup):
        self.logger.info("********* Test_003_AddCustomer *********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginpage = LoginPage(self.driver)
        self.loginpage.Enter_Username(self.username)
        self.loginpage.Enter_Password(self.password)
        self.loginpage.Click_Login()
        self.logger.info("*********** Login Successful **********")

        self.logger.info("********** starting Add Customer Test **********")
        self.addcustomer = AddCustomer(self.driver)
        self.addcustomer.Click_Custmermenu()
        self.addcustomer.Click_Customersubmenu()
        self.addcustomer.Click_AddNew()

        self.email = random_generator() + "@gmail.com"
        self.addcustomer.Enter_Email(self.email)
        self.addcustomer.Enter_Password("vinayak@123")
        self.addcustomer.Enter_FirstName("vinayak")
        self.addcustomer.Enter_LastName("kamati")
        self.addcustomer.Select_Gender("Male")
        self.addcustomer.Enter_DateofBirth("07/09/1997")
        self.addcustomer.Enter_CompanyName("VK Group")
        self.addcustomer.Select_Is_Tax_Exempt()
        self.addcustomer.Select_CustomerRole("Guest")
        self.addcustomer.Select_Vendors("Vendor 2")
        self.addcustomer.Select_Active()
        self.addcustomer.Enter_AdminComment("This is for testing")
        self.addcustomer.Click_Save()

        self.logger.info("*********** Saving Customer Info *****************")

        self.message = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissable").text
        if "The new customer has been added successfully." in self.message:
            assert True == True
            self.logger.info("******** Add Customer Test Passed ***********")
        else:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\nopCommerce application\\Screenshots\\Test_003_AddCustomer.png")
            self.logger.error("********** Add Customer Test Failed ***********")
            self.driver.close()

        self.driver.close()
        self.logger.info("*********** Ending Test_003_AddCustomer Test ***********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))