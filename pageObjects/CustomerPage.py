import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class CustomerPage:
    link_customer_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_sub_customer_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_add_new_xpath="//a[normalize-space()='Add new']"
    txt_email_xpath="//input[@id='Email']"
    text_password_xpath="//input[@id='Password']"
    radio_gender_male_xpath="//input[@id='Gender_Male']"
    radio_gender_female_xpath="//input[@id='Gender_Female']"
    text_dob_xapth="//input[@id='DateOfBirth']"
    listbox_customer_role_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    listbox_customer_role_administor_xpath="//li[normalize-space()='Administrators']"
    listbox_customer_role_guests_xpath="//li[normalize-space()='Guests']"
    btn_save_xpath="//button[@name='save']"
    txt_success_xpath="//div[@class='alert alert-success alert-dismissable']"

    def __init__(self,driver):
        self.driver=driver

    def addCustomer(self):
        self.driver.find_element(By.XPATH, self.link_customer_xpath).click()
        self.driver.find_element(By.XPATH, self.link_sub_customer_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_add_new_xpath).click()

    def email(self,emailid):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(emailid)

    def password(self,password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def selectGender(self,gender):
        if gender=="male":
            self.driver.find_element(By.XPATH, self.radio_gender_male_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.radio_gender_female_xpath).click()

    def customerRoles(self,role):
        if role=='guests':
            self.driver.find_element(By.XPATH, self.listbox_customer_role_xpath).click()
            self.driver.find_element(By.XPATH, self.listbox_customer_role_guests_xpath).click()
        elif role=="Administrators":
            self.driver.find_element(By.XPATH, self.listbox_customer_role_xpath).click()
            self.driver.find_element(By.XPATH, self.listbox_customer_role_administor_xpath).click()

    def savingForm(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def successmessage(self):
        self.driver.find_element(By.XPATH, self.txt_success_xpath)




