import os
import random
import string

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.CustomerPage import CustomerPage
from utilities.readConfigfile import Readconfig
from utilities.customlogger import loggen


class Test_003_addcustomer:
    url=Readconfig.url()
    username=Readconfig.username()
    password=Readconfig.password()

    # url = "https://admin-demo.nopcommerce.com/login"
    # username = "admin@yourstore.com"
    # password = "admin"

    log_er=loggen()

    @pytest.mark.regression
    def test_addnewcustomer(self,setup):
        self.log_er.info("*****Test login******")
        self.driver = setup
        self.driver.get(self.url)
        lp=LoginPage(self.driver)
        lp.username(self.username)
        lp.password(self.password)
        lp.click_login()

        cp=CustomerPage(self.driver)
        self.log_er.info("*****Test Add customer start******")
        cp.addCustomer()
        self.email=random_generator()+"@gmail.com"
        cp.email(self.email)
        cp.password("dummy")
        cp.selectGender("male")
        cp.customerRoles("guests")
        cp.savingForm()
        msg=cp.successmessage().text
        if msg=="The new customer has been added successfully.":
            assert True
            self.log_er.info("*****Add customer Passed******")
            self.driver.close()
        else:
            self.log_er.info("*****Add customer Failed******")
            self.driver.close()
            assert False


def random_generator(size=10,chars=string.ascii_lowercase+string.digits):
    str=""
    for i in range(size):
        str=str+(random.choice(chars))
    return str



