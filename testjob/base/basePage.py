from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.support.wait import WebDriverWait

#
class WebDriver(object):
    def __init__(self,driver):
        self.driver=driver

    def findElement(self,*loc):
        try:
            return WebDriverWait(self.driver,5).until(lambda x:x.find_element(*loc))
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def findElements(self,*loc):
        try:
            return WebDriverWait(self.driver,5).until(lambda x:x.find_elements(*loc))
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))
