from selenium.webdriver.common.by import By

class Admin():

    Admin_tag = (By.XPATH,"//span[text()='Admin']")
    AddUserButton = (By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']")
    UserroleDrop = (By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i")
    Empname = (By.XPATH, "//input[@placeholder='Type for hints...']")
    StatusDrop = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i")
    Username = (By.XPATH, "//label[text()='Username']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']/descendant::input")
    Password = (By.XPATH, "//label[text()='Password']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']/descendant::input")
    ConfirmPassword = (By.XPATH, "//label[text()='Confirm Password']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']/descendant::input")

    def __init__(self,driver):
        self.driver = driver

    def Click_on_admin(self):
        self.driver.find_element(*Admin.Admin_tag).click()

    def Click_add_user(self):
        self.driver.find_element(*Admin.AddUserButton).click()

    def select_userroledrop(self,value):
        self.driver.find_element(*Admin.UserroleDrop).click()
        option = self.driver.find_element(By.XPATH, f"//*[text()='{value}']")
        option.click()

    def select_statusdrop(self,value):
        self.driver.find_element(*Admin.StatusDrop).click()
        option = self.driver.find_element(By.XPATH, f"//*[text()='{value}']")
        option.click()

    def set_empname(self,value):
        self.driver.find_element(*Admin.Username).send_keys(f'{value}')

    def set_username(self,value):
        self.driver.find_element(*Admin.Username).send_keys(f'{value}')

    def set_password(self,value):
        self.driver.find_element(*Admin.Password).send_keys(f'{value}')

    def set_confirmPassword(self,value):
        self.driver.find_element(*Admin.ConfirmPassword).send_keys(f'{value}')

