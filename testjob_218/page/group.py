from base.basePage import *
from selenium.webdriver.common.by import By
from pywinauto import application
import time as t
import os

class groupMgt(WebDriver):

    #从首页到群管理页面
    menu = (By.CLASS_NAME,'ant-menu-submenu-title')
    group_mgt = (By.LINK_TEXT,u"群管理")

    #搜索群聊
    sourch_group = (By.CLASS_NAME,'ant-input')

    #群名称
    group_name = (By.XPATH,'//*[@class="ant-table-tbody"]/tr/td[2]/span')

    #群主
    group_host = (By.XPATH,'//*[@class="ant-table-tbody"]/tr/td[3]/span')

    #解散群聊入口
    dismiss_group_choose =(By.XPATH,'//*[@class="ant-table-tbody"]//*[@class="ant-checkbox-input"]')
    dismiss_group_button =(By.XPATH,'//button[contains(@class,"ant-btn-primary")]')
    dismiss_group_text=(By.XPATH,'//*[@class="ant-table-body"]//span[text()="解散群"]')#集合
    dismiss_group_submit =(By.XPATH,'//*[@class="ant-modal-content"]//button[contains(@class,"ant-btn-primary")]')#使用索引1的元素

    #变更群主
    change_group_host=(By.XPATH,'//*[@class="ant-table-body"]//span[text()="变更群主"]')#集合
    change_group_host_check=(By.XPATH,'//*[@class="tree-main"]//div[contains(@class,"tree-children-ul")]')#集合
    change_group_host_name=(By.XPATH,'//*[@class="tree-main"]//*[@class="tree-children-info-name"]')#集合
    change_group_host_submit=(By.CLASS_NAME,'zy-button zy-button--primary')

    @property
    def gotoGroup(self):
        self.findElements(*self.menu)[0].click()
        self.findElement(*self.group_mgt).click()
        t.sleep(2)

    def searchGroup(self,name):
        self.findElement(*self.sourch_group).send_keys(name)
        try:
            self.findElements(*self.group_name)
        except:
            return ['null']
        else:
            return self.findElements(*self.group_name)

    def dismissGroupOne(self):#按钮执行
        pass

    def dismissGroupTwo(self):#操作执行
        pass

    def changeGroupHost(self):
        pass
