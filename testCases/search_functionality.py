from testCases.login_test import TestClass1
from PageObjects.DashboardPage import Search
from PageObjects.LoginPage import LoginHrm


class TestClass2(TestClass1):

    def test_search_box_02(self,setup):
        self.driver = setup
        self.login = LoginHrm(self.driver)
        self.driver.implicitly_wait(80)
        self.login.User_login("Admin","admin123")
        self.search = Search(self.driver)
        self.search.Search_Box("Time")
        self.search.Button_Search()
        self.search.Verify_Searched()
        self.search.Enter_Time_Module()
        self.search.Time_Module_Page()
        print("code run successfull")
