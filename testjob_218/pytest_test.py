from selenium import webdriver
from time import sleep,ctime
from thread_param import *
import yaml
from utils.operationData import *
import unittest

class Testnew(unittest.TestCase,OperationData):

    # def __init__(self, host, bowser):
    #     super().__init__()
    #     self.host=host
    #     self.bowser = bowser

    def setup(self):
        dict=OperationData().getYamlData()['browsers']
        for i in range(len(dict)):
            print(dict[i]['host'])
            print(dict[i]['browser'])
            dc = {'browserName': dict[i]['browser']}
            self.driver = webdriver.Remote(dict[i]['host'], desired_capabilities=dc)
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id("kw").send_keys('chrome')
        self.driver.find_element_by_id("su").click()
        print('1')

    def teardown(self):
        print('2')
        #self.driver.quit()


if __name__ == '__main__':
    #thread_browser(Testnew.setup)
#     pytest.main(['-sv','pytest_test.py'])
    unittest.main()