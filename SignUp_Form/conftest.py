import time

import pytest
from selenium import webdriver

@pytest.fixture()
def setUp(request):
    driver=webdriver.Chrome(executable_path="C:\\Users\\Sumit\\Desktop\\Chromedriver\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    request.cls.driver=driver
    yield
    time.sleep(4)
    driver.close()