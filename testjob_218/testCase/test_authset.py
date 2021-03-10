import unittest
from selenium import webdriver
from page.authset import *
from utils.operationData import *
from ddt import ddt,unpack,data
import time as t


class authSetTest(unittest.TestCase,AuthSet,OperationData):
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

    def test_1_gotoAuthSetMgt(self):
        self.gotoAuthSet

    def test_2_addRole(self):
        self.assertIn("新角色", self.addNewRole())

    def test_3_editRole(self):
        self.assertIn("close",self.editRole())

    def test_4_deleteRole(self):
        self.assertIn("普通",self.deleteRole())


