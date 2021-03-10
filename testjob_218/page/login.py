from base.basePage import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import gc
from selenium.webdriver.common.keys import Keys


class management(WebDriver):
    username_loc=(By.ID,'userName')
    password_loc=(By.ID,'password')
    login_click=(By.XPATH,'//*[@id="Management2"]/div/div/div[1]/div/div[2]/form/div/div[3]/button')
    login_error_loc=(By.CLASS_NAME,'ant-message-notice')
    login_error_loc2=(By.CLASS_NAME,'ant-form-explain')
    login_success_loc=(By.CLASS_NAME,'ant-dropdown-link')

    def typeUsername(self,username):
        self.findElement(*self.username_loc).send_keys(username)

    def typePassword(self,password):
        self.findElement(*self.password_loc).send_keys(password)

    @property
    def clickLogin(self):
        gc.collect()
        self.findElement(*self.login_click).click()

    def clearUsername(self):
        self.findElement(*self.username_loc).send_keys(Keys.CONTROL,'a')
        self.findElement(*self.username_loc).send_keys(Keys.DELETE)

    def clearPassword(self):
        self.findElement(*self.password_loc).send_keys(Keys.CONTROL,'a')
        self.findElement(*self.password_loc).send_keys(Keys.DELETE)

    def login(self,username,password):
        self.clearUsername()
        self.typeUsername(username)
        self.clearPassword()
        self.typePassword(password)
        self.clickLogin

    def loginError(self,username,password):
        if (username == '') or (password == ''):
            return self.findElements(*self.login_error_loc2)[0].text
        else:
            try:
                return self.findElement(*self.login_error_loc).text
            except:
                return self.findElement(*self.login_success_loc).text
