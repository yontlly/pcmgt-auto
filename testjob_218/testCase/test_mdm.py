import unittest
from selenium import webdriver
from page.account import *
from page.mdm import *
from utils.operationData import *
from ddt import ddt,unpack,data
import time as t


class mdmTest(unittest.TestCase,Account,Mdm,OperationData):
    @classmethod
    def setUpClass(cls):
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
        cls.driver = webdriver.Chrome(executable_path=chrome_path)
        cls.driver.get('http://10.206.83.102:8787/pc-management/#/login')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.find_element_by_id('userName').send_keys('yanghua')
        cls.driver.find_element_by_id('password').send_keys('11111112')
        cls.driver.find_element_by_xpath('//*[@class="ant-btn login-form-button ant-btn-primary"]').click()

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        pass

    #建成员
    # def test_1_gotoMdmMgt(self):
    #     self.gotoAccountMgt
    #     t.sleep(2)
    #     self.addDept("设备管理部门")
    #     t.sleep(2)
    #     self.addUser("设备成员")
    #     t.sleep(2)
    #     self.gotoMdm

    def test_2_createTactics(self):
        t.sleep(2)
        self.gotoMdm
        t.sleep(2)
        self.createTactics(client='移动,web',name='设备成员')