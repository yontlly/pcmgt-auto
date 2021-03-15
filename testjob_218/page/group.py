from base.basePage import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from pywinauto import application
import time as t
import os

class groupMgt(WebDriver):

    #从首页到群管理页面
    menu = (By.CLASS_NAME,'ant-menu-submenu-title')
    group_mgt = (By.LINK_TEXT,u"群管理")

    #搜索群聊
    search_group = (By.CLASS_NAME,'ant-input')

    #群名称
    group_name = (By.XPATH,'//*[@class="ant-table-tbody"]/tr/td[2]/span[2]')

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
    change_group_host_submit=(By.XPATH,'//button[contains(@class,"zy-button--primary")]')

    search_result=[]
    search_result_count=0

    @property
    def gotoGroup(self):
        self.findElements(*self.menu)[0].click()
        self.findElement(*self.group_mgt).click()
        t.sleep(2)

    def searchGroup(self,name):
        self.findElement(*self.search_group).send_keys(name)
        t.sleep(2)
        try:
            self.findElements(*self.group_name)
        except:
            self.search_result.append('null')
        else:
            for i in range(len(self.findElements(*self.group_name))):
                self.search_result.append(self.findElements(*self.group_name)[i].text)
        return self.search_result


    def dismissGroupOne(self):#按钮执行
        self.search_result_count = len(self.findElements(*self.group_name))
        try:
            self.findElements(*self.dismiss_group_choose)[0].click()
            self.findElement(*self.dismiss_group_button).click()
            self.findElements(*self.dismiss_group_submit)[-1].click()
            t.sleep(4)
            self.findElements(*self.group_name)
        except:
            self.search_result=['data/service failer']
        else:
            if(self.search_result_count-1 == len(self.findElements(*self.group_name))):
                for i in range(len(self.findElements(*self.group_name))):
                    self.search_result.append(self.findElements(*self.group_name)[i].text)
            else:
                self.search_result = ['dismissGroupOne case failure']
        return self.search_result

    def dismissGroupTwo(self):#操作执行
        try:
            self.findElements(*self.dismiss_group_text)[0].click()
            self.findElements(*self.dismiss_group_submit)[-1].click()
            t.sleep(4)
            self.findElements(*self.group_name)
        except:
            self.search_result=['null']
        else:
            for i in range(len(self.findElements(*self.group_name))):
                self.search_result.append(self.findElements(*self.group_name)[i].text)
        return self.search_result

    # def changeGroupHost(self,name):#最优解
    #     old_group_host=self.findElements(*self.group_host)[0].text
    #     self.findElements(*self.change_group_host)[0].click()
    #     t.sleep(2)
    #     self.findElements(*self.change_group_host_check)[0].click()
    #     self.findElement(*self.change_group_host_submit).click()
    #     t.sleep(2)
    #     self.driver.getLocalStorage().clear()
    #     self.driver.refresh()
    #     t.sleep(2)
    #     self.findElement(*self.search_group).send_keys(name)
    #     t.sleep(2)
    #     new_group_host=self.findElements(*self.group_host)[0].text
    #     if old_group_host == new_group_host:
    #         return 'change group_host false'
    #     else:
    #         return 'change group_host true'

    def changeGroupHost(self,name):
        old_group_host=self.findElements(*self.group_host)[0].text
        self.findElements(*self.change_group_host)[0].click()
        t.sleep(2)
        self.findElements(*self.change_group_host_check)[0].click()
        self.findElement(*self.change_group_host_submit).click()
        self.driver.refresh()
        t.sleep(2)
        new_group_host=self.findElements(By.XPATH,'//span[contains(text(),"'+name+'")]/../../../td[3]/span')[0].text
        if old_group_host == new_group_host:
            return 'change group_host false'
        else:
            return 'change group_host true'
