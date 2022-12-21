import os
import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        # driver = webdriver.Chrome()
        driver=webdriver.Chrome(ChromeDriverManager().install())
        print("launching Chrome browser")
    else:
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("**Parameter not matching ,so running in chrome**")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



#########Pytest html report hook###########

def pytest_configure(config): #Environemntal details
    config._metadata['Project name']='nop commerce'
    config._metadata['Module name'] = 'Customers'
    config._metadata['Tester name'] = 'Kishore'
    config._metadata['Date'] = time.asctime()


def pytest_metadata(metadata): #delete/modify environment
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)

def pytest_html_report_title(report):
   report.title ="Report"










