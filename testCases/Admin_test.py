from PageObjects.AdminPage import Admin
from testCases.login_test import TestClass1
from PageObjects.DashboardPage import Search
from PageObjects.LoginPage import LoginHrm

class Test_admin(TestClass1):

    def test_add_user_03(self,setup):
        self.driver = setup
        self.login = LoginHrm(self.driver)
        self.driver.implicitly_wait(80)
        self.login.User_login("Admin", "admin123")
        self.admin = Admin(self.driver)
        self.admin.Admin_tag()
        self.admin.AddUserButton()
        self.admin.select_userroledrop('ESS')
        self.admin.set_empname('jack')
        self.admin.select_statusdrop('Enabled')
        self.admin.set_username("jack159")
        self.admin.set_password("Qwerty@123")
        self.admin.set_confirmPassword("Qwerty@123")


