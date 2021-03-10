from base.basePage import *
from selenium.webdriver.common.by import By
from pywinauto import application
import time as t
import os


class AuthSet(WebDriver):

    #从首页到角色权限页面
    menu = (By.CLASS_NAME,'ant-menu-submenu-title')
    auth_set = (By.LINK_TEXT,u"角色权限")

    #遍历所有角色
    role_item=(By.XPATH,'//*[@class="authSetting"]//li[contains(@class,"ant-menu-item")]')#0：组织管理员

    #添加新角色
    add_new_role_button=(By.XPATH,'//*[@class="anticon anticon-plus"]')

    #新建角色按钮
    add_new_role_name=(By.XPATH,'//input[contains(@class,"ant-input-lg")]')
    add_new_role_submit=(By.XPATH,'//*[@class="ant-modal-content"]//button[contains(@class,"ant-btn-primary")]')

    #编辑角色按钮
    edit_role_button=(By.XPATH,'//*[@class="authSetting"]//button[contains(@class,"ant-btn-primary")]')
    edit_role_content=(By.XPATH,'//span[text()="允许使用帐号管理"]')
    #edit_role_content_check = (By.XPATH, '//span[text()="允许使用帐号管理"]/../span[contains(@class,"ant-checkbox-checked")]')
    edit_role_submit=(By.XPATH,'//*[@class="authSetting"]//button[contains(@class,"ant-btn-primary")]')
    role_checkbox=(By.XPATH,'//input[contains(@class,"ant-checkbox-input")]')#集合，用于勾选“可由其他管理员分配”

    #删除角色按钮
    delete_role_button=(By.XPATH,'//button[contains(@class,"ant-btn-default")]')
    delete_role_submit=(By.XPATH,'//*[@class="ant-modal-content"]//button[contains(@class,"ant-btn-primary")]')

    #移交权限（最后一步）

    operating_hints_loc = (By.CLASS_NAME, 'ant-message-notice')#操作提示

    @property
    def gotoAuthSet(self):
        self.findElements(*self.menu)[0].click()
        self.findElement(*self.auth_set).click()
        t.sleep(2)

    def addNewRole(self):
        self.findElement(*self.add_new_role_button).click()
        self.findElements(*self.add_new_role_name)[-1].send_keys(u"新角色")
        self.findElements(*self.add_new_role_submit)[-1].click()
        t.sleep(2)
        return self.findElements(*self.role_item)[-1].text

    def editRole(self):
        self.findElements(*self.role_item)[-1].click()
        self.findElement(*self.edit_role_button).click()
        self.findElement(*self.edit_role_content).click()
        self.findElement(*self.edit_role_submit).click()

        #检查帐号管理权限是否已经关闭
        try:
            self.findElements(By.XPATH, '//span[text()="允许使用帐号管理"]/../span[contains(@class,"ant-checkbox-checked")]')
        except:
            return "close"
        else:
            return "open"

    def deleteRole(self):
        self.findElements(*self.role_item)[-1].click()
        self.findElement(*self.delete_role_button).click()
        self.findElement(*self.delete_role_submit).click()
        t.sleep(2)
        return self.findElements(*self.role_item)[-1].text

    @property
    def operatingHints(self):
        return self.findElements(*self.operating_hints_loc)[-1].text