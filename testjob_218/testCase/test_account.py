import unittest
from selenium import webdriver
from page.account import *
from utils.operationData import *
from ddt import ddt,unpack,data
import time as t



@ddt
class accountTest(unittest.TestCase,Account,OperationData):
    @classmethod
    def setUpClass(cls):
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
        cls.driver = webdriver.Chrome(executable_path=chrome_path)
        cls.driver.get('http://192.168.1.165:8787/pc-management/#/login')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.find_element_by_id('userName').send_keys('yanghua275')
        cls.driver.find_element_by_id('password').send_keys('Aa123123')
        cls.driver.find_element_by_xpath('//*[@class="ant-btn login-form-button ant-btn-primary"]').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        #pass

    def test_1_gotoAccountMgt(self):
        self.gotoAccountMgt

    def test_2_addDept(self,name="自动化"):
        t.sleep(2)
        self.addDept(name)
        self.assertIn("成功",self.operatingHints)

    def test_3_editDept(self,name="自动化II"):
        t.sleep(2)
        self.editDept(name)
        self.assertIn("成功",self.operatingHints)

    def test_4_addUser(self,name="自动化人员"):
        t.sleep(2)
        self.addUser(name)

    def test_5_editUser(self,name="自动化人员II"):
        t.sleep(2)
        self.editUser(name)

    def test_6_deleteUserOne(self):
        t.sleep(2)
        self.deleteUser_one()

    def test_7_deleteUsertwo(self):
        t.sleep(2)
        self.deleteUser_two()

    def test_deleteDept(self):
        t.sleep(2)
        self.deleteDept()
        #self.assertIn("成功",self.operatingHints)