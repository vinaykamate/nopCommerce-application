from selenium.webdriver.common.by import By


class SearchCustomer:
    textbox_email_cssselector = "#SearchEmail"
    textbox_firstname_cssselector = "#SearchFirstName"
    textbox_lastname_cssselector = "#SearchLastName"
    button_search_cssselector = "#search-customers"

    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']/tbody/tr"
    tablecolumn_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_email_cssselector).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_email_cssselector).send_keys(email)

    def Enter_FName(self, fname):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_firstname_cssselector).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_firstname_cssselector).send_keys(fname)

    def Enter_LName(self, lname):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_lastname_cssselector).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_lastname_cssselector).send_keys(lname)

    def Click_Search(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_search_cssselector).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tablecolumn_xpath))

    def SearchCustomerByEmail(self, email):
        flag = False
        for i in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(i)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def SearchCustomerByName(self, Name):
        flag = False
        for i in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(i) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag


