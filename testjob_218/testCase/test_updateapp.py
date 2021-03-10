import unittest
from selenium import webdriver
from page.importversion import *
from utils.operationData import *
from ddt import ddt,unpack,data
import time as t
from selenium.webdriver.support.wait import WebDriverWait
from ext_method.killprocess import *



@ddt
class loginUpdateapp(unittest.TestCase,management_updateapp,OperationData,KillProcess):
    @classmethod
    def setUpClass(cls):
        cls.kill_process(name="chrome.exe")
        t.sleep(2)
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
        cls.driver = webdriver.Chrome(executable_path=chrome_path)
        #cls.driver=webdriver.Chrome()
        cls.driver.get('http://10.206.104.218:8787/pc-management/#/login')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        cls.driver.find_element_by_id('userName').send_keys('masteradmin')
        cls.driver.find_element_by_id('password').send_keys('!234Qwer')
        cls.driver.find_element_by_xpath('//*[@id="Management2"]/div/div/div[1]/div/div[2]/form/div/div[3]/button').click()
        #self.clickupdatepage
        WebDriverWait(cls.driver, 30).until(lambda x: cls.driver.find_elements_by_class_name("item-title")[2]).click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*OperationData().getData("2"))
    @unpack
    def test_1(self,order,path,reSult):
        self.clickupdateapp(order,path)
        t.sleep(1)
        self.assertIn(reSult,self.updateError)
        t.sleep(2)




if '__name__'=='__main__':
    unittest.main(verbosity=2)