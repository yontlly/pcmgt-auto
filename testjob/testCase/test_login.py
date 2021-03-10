import unittest
from selenium import webdriver
from page.login import *
from utils.operationData import *
from ddt import ddt,unpack,data
import time



@ddt
class loginTest(unittest.TestCase,management,OperationData):
    def setUp(self):
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=chrome_path)
        #self.driver=webdriver.Chrome()
        self.driver.get('http://10.206.104.220:8787/pc-management/#/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="Management2"]/div/div/div[1]/div/div[2]/div[1]').click()


    def tearDown(self):
        self.driver.quit()

    @data(*OperationData().getData("1"))
    @unpack
    def test_1(self,userName,passWord,reSult):
        self.login(userName,passWord)
        time.sleep(1)
        self.assertIn(reSult,self.loginError(userName,passWord))


if '__name__'=='__main__':
    unittest.main(verbosity=2)