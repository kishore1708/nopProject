import os

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readConfigfile import Readconfig
from utilities.customlogger import loggen


class Test_001_login:
    url=Readconfig.url()
    username=Readconfig.username()
    password=Readconfig.password()

    # url = "https://admin-demo.nopcommerce.com/login"
    # username = "admin@yourstore.com"
    # password = "admin"

    log_er=loggen()

    @pytest.mark.sanity
    def test_homepage_title(self,setup):
        self.log_er.info("*******Test homepage title******")
        self.driver=setup
        self.driver.get(self.url)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.log_er.info("Passed")
            self.driver.close()
        else:
            self.driver.save_screenshot("../screenshots/" + "test_homepage_title.png")
            self.log_er.info("Failed")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.log_er.info("*****Test login******")
        self.driver = setup
        self.driver.get(self.url)
        lp=LoginPage(self.driver)
        lp.username(self.username)
        lp.password(self.password)
        lp.click_login()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.log_er.info("Passed")
            self.driver.close()
        else:
            self.driver.save_screenshot("../screenshots/"+"test_login.png")
            self.log_er.info("Failed")
            self.driver.close()
            assert False

