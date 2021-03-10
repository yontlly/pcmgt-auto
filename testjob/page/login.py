from base.basePage import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class management(WebDriver):
    username_loc=(By.ID,'userName')
    password_loc=(By.ID,'password')
    login_click=(By.XPATH,'//*[@id="Management2"]/div/div/div[1]/div/div[2]/form/div/div[3]/button')
    login_error_loc=(By.XPATH,'/html/body/div[3]/div/span')
    login_error_loc2=(By.CLASS_NAME,'ant-form-explain')
    login_success_loc=(By.CLASS_NAME,'ant-dropdown-link')

    def typeUsername(self,username):
        self.findElement(*self.username_loc).send_keys(username)

    def typePassword(self,password):
        self.findElement(*self.password_loc).send_keys(password)

    @property
    def clickLogin(self):
        self.findElement(*self.login_click).click()

    def clearUsername(self):
        self.findElement(*self.username_loc).clear()

    def clearPassword(self):
        self.findElement(*self.password_loc).clear()

    def login(self,username,password):
        self.clearUsername()
        self.clearPassword()
        self.typeUsername(username)
        self.typePassword(password)
        self.clickLogin

    #@property
    def loginError(self,username,password):
        if (username == '') or (password == ''):
            return self.findElements(*self.login_error_loc2)[0].text
        else:
            try:
                return self.findElement(*self.login_error_loc).text
            except:
                return self.findElement(*self.login_success_loc).text
