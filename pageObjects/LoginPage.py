from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_email_xpath="//input[@id='Email']"
    textbox_password_xpath="//input[@id='Password']"
    btn_login_xpath="//button[normalize-space()='Log in']"
    btn_logout_xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def username(self,uname):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).send_keys(uname)

    def password(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()
