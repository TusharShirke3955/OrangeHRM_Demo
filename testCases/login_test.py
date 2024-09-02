import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.LoginPage import LoginHrm
# @pytest.fixture
class TestClass1:

    def test_login_01(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(80)
        self.login = LoginHrm(self.driver)
        self.login.User_login("Admin","admin123")
        self.login.Verify_Login()
        self.driver.quit()

