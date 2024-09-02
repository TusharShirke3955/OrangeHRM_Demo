from selenium import webdriver
from selenium.webdriver.common.by import By



class Search():
    Search_Box_XPATH = (By.XPATH, "//input[@placeholder='Search']")
    Search_Button_XPATH = (By.XPATH, "//div[@class='oxd-main-menu-search']//*[name()='svg']")
    Verify_Time_XPATH = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
    Click_Time_XPATH = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
    Time_Page_XPATH = (By.XPATH, "//div[@class='orangehrm-header-container']")


    def __init__(self,driver):
        self.driver = driver
    def Search_Box(self,search):
        self.driver.find_element(*Search.Search_Box_XPATH).send_keys(search)

    def Button_Search(self):
        self.driver.find_element(*Search.Search_Button_XPATH).click()

    def Verify_Searched(self):
        tim = self.driver.find_element(*Search.Verify_Time_XPATH)
        if tim.is_displayed():
            assert True
        else:
            assert False

    def Enter_Time_Module(self):
        self.driver.find_element(*Search.Click_Time_XPATH).click()

    def Time_Module_Page(self):
        timepage = self.driver.find_element(*Search.Time_Page_XPATH)
        if timepage.is_displayed():
            assert True
        else:
            assert False