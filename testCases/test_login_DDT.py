import os

from pageObjects.LoginPage import LoginPage
from utilities.readConfigfile import Readconfig
from utilities.customlogger import loggen
from utilities import excelutil


class Test_001_login:
    url=Readconfig.url()
    # username=Readconfig.username()
    # password=Readconfig.password()

    # url = "https://admin-demo.nopcommerce.com/login"
    # username = "admin@yourstore.com"
    # password = "admin"

    log_er=loggen()

    def test_login(self,setup):
        self.log_er.info("*****Test login******")
        self.driver = setup
        self.driver.get(self.url)
        lp=LoginPage(self.driver)

        row=excelutil.getRowcount("../testData/Book3.xlsx","Sheet1")
        lst=[]
        for r in range(2,row+1):
            user=excelutil.readData("../testData/Book3.xlsx","Sheet1",r,1)
            password=excelutil.readData("../testData/Book3.xlsx","Sheet1",r,2)
            status = excelutil.readData("../testData/Book3.xlsx", "Sheet1", r, 3)
            lp.username(user)
            lp.password(password)
            lp.click_login()
            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if status=='Pass':
                    assert True
                    lp.click_logout()
                    lst.append("Pass")
                elif status=='Fail':
                    self.log_er.info("Passed")
                    lp.click_logout()
                    lst.append("Fail")
            elif act_title != "Dashboard / nopCommerce administration":
                if status=='Pass':
                    assert True
                    lst.append("Fail")
                elif status=='Fail':
                    lst.append("Pass")
        if "Fail" not in lst:
            self.log_er.info("***Test passed***")
            self.driver.close()
            assert True
        else:
            self.log_er.info("***Test Failed***")
            self.driver.close()
            assert False


