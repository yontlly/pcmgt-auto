import unittest
from selenium import webdriver
from page.login import *
from utils.operationData import *
from ddt import ddt,unpack,data
import time



@ddt
class loginTest(unittest.TestCase,management,OperationData):
    @classmethod
    def setUpClass(cls):
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
        cls.driver = webdriver.Chrome(executable_path=chrome_path)
        #self.driver=webdriver.Chrome()
        cls.driver.get('http://10.206.104.220:8787/pc-management/#/login')
        cls.driver.maximize_window()
        #cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*OperationData().getData("1"))
    @unpack
    def test_1(self,userName,passWord,reSult):
        self.driver.delete_all_cookies()
        self.login(userName,passWord)
        time.sleep(3)
        self.assertIn(reSult,self.loginError(userName,passWord))

if '__name__'=='__main__':
    unittest.main(verbosity=2)