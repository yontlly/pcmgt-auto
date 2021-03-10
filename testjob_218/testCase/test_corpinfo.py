import unittest
from selenium import webdriver
from page.corpinfo import *
from utils.operationData import *
from ddt import ddt,unpack,data
import time as t


@ddt
class corpInfoTest(unittest.TestCase,CorpInfo,OperationData):
    @classmethod
    def setUpClass(cls):
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
        cls.driver = webdriver.Chrome(executable_path=chrome_path)
        cls.driver.get('http://10.206.83.102:8787/pc-management/#/login')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        cls.driver.find_element_by_id('userName').send_keys('yanghua')
        cls.driver.find_element_by_id('password').send_keys('11111112')
        cls.driver.find_element_by_xpath('//*[@class="ant-btn login-form-button ant-btn-primary"]').click()

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        pass

    def test_1_gotoAccountMgt(self):
        self.gotoCorpinfo

    @data(*OperationData().getData("3"))
    @unpack
    def test_2(self,*args):
        self.editCorpInfo(*args)
        t.sleep(2)
        self.assertIs("操作成功",self.operatingHints)



