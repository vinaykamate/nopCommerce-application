from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_cssselector = "#Email"
    textbox_password_cssselector = "#Password"
    button_login_cssselector = ".button-1.login-button"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_cssselector).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_cssselector).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_cssselector).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_cssselector).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_login_cssselector).click()

    def Click_Logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
