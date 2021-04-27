from base.basePage import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from pywinauto import application
import time as t
from enum import Enum
from selenium.webdriver.common.keys import Keys


class TacticsClient(Enum):
    windows = win = pc = 桌面端 = 桌面 = ['Windows']
    mac = ['Mac']
    android = ['Android']
    ios = ['iOS']
    web = ['Web']
    移动端 = 移动 = ['Android','iOS']


class Mdm(WebDriver):
    #从首页到账户管理页面
    menu = (By.CLASS_NAME,'ant-menu-submenu-title')
    mdm_mgt = (By.LINK_TEXT,u"策略及应用")

    #添加策略
    add_tactics_button = (By.CLASS_NAME,'ant-btn')

    #选择类型
    choose_type= (By.CLASS_NAME,'ant-select-selection__placeholder')
    choose_client_type=(By.XPATH,'//li[contains(text(),"客户端类型")]')
    choose_client_type_equal=(By.XPATH,'//li[contains(text(),"等于")]')
    choose_client_type_notequal=(By.XPATH,'//li[contains(text(),"不等于")]')

    choose_account_type=(By.XPATH,'//li[contains(text(),"自定义帐号")]')
    choose_account_type_equal=(By.XPATH,'//li[contains(text(),"包含")]')
    choose_account_type_notequal=(By.XPATH,'//li[contains(text(),"不包含")]')

    #添加筛选条件
    add_choose_type = (By.CLASS_NAME,'add-condition')

    #客户端类型
    def ChooseClient(self, client:str):
        b=[]
        choose_client = []
        for i in client.split(','):
            b += TacticsClient[i.lower()].value
        for i in b:
            choose_client.append('//span[contains(text(),\"'+i+'\")]')
        return choose_client

    #自定义帐号
    choose_person = (By.CLASS_NAME,'rangechoice')
    search_person =(By.ID,'male')
    choose_person_checkbox=(By.XPATH,'//*[@class="zy-tree-search-list scroll"]//*[@class="zy-circle tree-checkbox false"]')
    change_person_submit=(By.XPATH,'//button[contains(@class,"zy-button--primary")]')

    #编辑/保存按钮
    tactics_submit = (By.XPATH,'//*button[@class="ant-btn ant-btn-primary"]')

    # 启用禁用
    tactics_use = (By.XPATH, '//span[@class="ant-switch ant-switch-checked"]')

    @property
    def gotoMdm(self):
        self.findElements(*self.menu)[3].click()
        self.findElement(*self.mdm_mgt).click()
        t.sleep(2)

    def createTactics(self,client:str,name:str):
        for i in range(2):
            #添加策略
            self.findElement(*self.add_tactics_button).click()
            #选择客户端
            self.findElements(*self.choose_type)[4*i].click()
            self.findElements(*self.choose_client_type)[-1].click()
            #等于/不等于
            # self.findElements(*self.choose_type)[4*i+1].click()
            # self.findElement(*self.choose_client_type_equal).click()
            # self.findElement(*self.choose_client_type_notequal).click()
            #选择端
            for choose_client in self.ChooseClient(client):
                self.findElement(*(By.XPATH,choose_client)).click()
            #添加筛选条件
            self.findElements(*self.add_choose_type)[-1].click()
            #选择自定义账号
            self.findElements(*self.choose_type)[4*i+2].click()
            self.findElements(*self.choose_account_type)[-1].click()
            #包含/不包含
            # self.findElements(*self.choose_type)[4*i+3].click()
            # self.findElement(*self.choose_account_type_equal).click()
            # self.findElement(*self.choose_account_type_notequal).click()
            #选人
            self.findElement(*self.choose_person).click()
            t.sleep(2)
            self.findElement(*self.search_person).send_keys(name)
            t.sleep(2)
            self.findElements(*self.choose_person_checkbox)[-1].click()
            self.findElement(*self.change_person_submit).click()
            #保存策略
            self.findElements(*self.tactics_submit)[-1].click()
            #启用禁用策略
            if i>0:self.findElements(*self.tactics_use)[-1].click()