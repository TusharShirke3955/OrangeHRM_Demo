from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginHrm():
    Text_Username_XPATH = (By.XPATH,"//input[@placeholder='Username']")
    Text_Password_XPATH = (By.XPATH,"//input[@placeholder='Password']")
    Button_Login_XPATH = (By.XPATH,"//button[@type='submit']")
    Verify_Login_XPATH = (By.XPATH,"//*[name()='path' and contains(@d,'M 480.469 ')]")


    def __init__(self,driver):
        self.driver = driver



    def Verify_Login(self):

        verify = self.driver.find_element(*LoginHrm.Verify_Login_XPATH)
        if verify.is_displayed():
            assert True
        else:
            assert False

    def Search_Box(self,search):
        self.driver.find_element(*LoginHrm.Search_Box_XPATH).send_keys(search)

    def Button_Search(self):
        self.driver.find_element(*LoginHrm.Search_Button_XPATH).click()

    def Verify_Searched(self):
        tim = self.driver.find_element(*LoginHrm.Verify_Time_XPATH)
        if tim.is_displayed():
            assert True
        else:
            assert False

    def Enter_Time_Module(self):
        self.driver.find_element(*LoginHrm.Click_Time_XPATH).click()

    def Time_Module_Page(self):
        timepage = self.driver.find_element(*LoginHrm.Time_Page_XPATH)
        if timepage.is_displayed():
            assert True
        else:
            assert False

    def User_login(self,username,password):
        self.driver.find_element(*LoginHrm.Text_Username_XPATH).send_keys(username)
        self.driver.find_element(*LoginHrm.Text_Password_XPATH).send_keys(password)
        self.driver.find_element(*LoginHrm.Button_Login_XPATH).click()