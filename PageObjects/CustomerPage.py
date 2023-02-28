import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    link_customermenuitem_xpath = "//i[@class='nav-icon far fa-user']"
    link_customersubmenuitem_xpath = "//a[@href='/Admin/Customer/List']"
    link_addnewcustomer_xpath = "//i[@class='fas fa-plus-square']"

    textbox_email_cssselector = "#Email"
    textbox_password_cssselector = "#Password"
    textbox_firstname_cssselector = "#FirstName"
    textbox_lastname_cssselector = "#LastName"
    radiobtn_gendermale_cssselector = "#Gender_Male"
    radiobtn_genderfemale_cssselector = "#Gender_Female"
    textbox_dateofbirth_cssselector = "#DateOfBirth"
    textbox_companyname_cssselector = "#Company"
    checkbox_istaxexempt_cssselector = "#IsTaxExempt"
    text_customerroles_remove_default_xpath = "//span[@title='delete']"
    text_customerroles_xpath = "(//div[@role='listbox'])[2]"
    list_admistrator_xpath = "//li[normalize-space()='Administrators']"
    list_forummoderator_xpath = "//li[normalize-space()='Forum Moderators']"
    list_guest_xpath = "//li[normalize-space()='Guests']"
    list_registered_xpath = "//li[normalize-space()='Registered']"
    list_vendors_xpath = "//li[@id='ef73f39c-3e71-44a3-a764-b1317f11a769']"
    select_managervendor_cssselector = "#VendorId"
    checkbox_active_cssselector = "#Active"
    textbox_admincomment_cssselector = "#AdminComment"
    button_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def Click_Custmermenu(self):
        self.driver.find_element(By.XPATH, self.link_customermenuitem_xpath).click()

    def Click_Customersubmenu(self):
        self.driver.find_element(By.XPATH, self.link_customersubmenuitem_xpath).click()

    def Click_AddNew(self):
        self.driver.find_element(By.XPATH, self.link_addnewcustomer_xpath).click()

    def Enter_Email(self, email):
        self.driver.find_element(By.CSS_SELECTOR,self.textbox_email_cssselector).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_cssselector).send_keys(password)

    def Enter_FirstName(self, firstname):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_firstname_cssselector).send_keys(firstname)

    def Enter_LastName(self, lastname):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_lastname_cssselector).send_keys(lastname)

    def Select_Gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.CSS_SELECTOR,self.radiobtn_gendermale_cssselector).click()
        elif gender == 'Female':
            self.driver.find_element(By.CSS_SELECTOR, self.radiobtn_genderfemale_cssselector).click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, self.radiobtn_gendermale_cssselector).click()

    def Enter_DateofBirth(self, dob):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_dateofbirth_cssselector).send_keys(dob)

    def Enter_CompanyName(self, companyname):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_companyname_cssselector).send_keys(companyname)

    def Select_Is_Tax_Exempt(self):
        self.driver.find_element(By.CSS_SELECTOR, self.checkbox_istaxexempt_cssselector).click()

    def Select_CustomerRole(self, role):
        self.driver.find_element(By.XPATH, self.text_customerroles_remove_default_xpath).click()
        self.driver.find_element(By.XPATH, self.text_customerroles_xpath).click()
        time.sleep(3)
        if role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.list_admistrator_xpath)
        elif role == "Forrum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.list_forummoderator_xpath)
        elif role == "Guests":
            self.listitem = self.driver.find_element(By.XPATH, self.list_guest_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.list_registered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.list_vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.list_guest_xpath)
        time.sleep(2)
        self.listitem.click()
        # self.driver.execute_script("arguments[0].click;", self.listitem)

    def Select_Vendors(self, vendor):
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, self.select_managervendor_cssselector))
        dropdown.select_by_visible_text(vendor)

    def Select_Active(self):
        self.driver.find_element(By.CSS_SELECTOR, self.checkbox_active_cssselector).click()

    def Enter_AdminComment(self, admincomment):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_admincomment_cssselector).send_keys(admincomment)

    def Click_Save(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()
