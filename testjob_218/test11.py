import time as t
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from pywinauto import application
from ext_method.findFileByDate import *

chrome_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
driver= webdriver.Chrome(executable_path=chrome_path)
driver.get('http://10.206.104.220:8787/pc-management/#/login')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id('userName').send_keys('yanghua')
driver.find_element_by_id('password').send_keys('11111112')
driver.find_element_by_xpath('//*[@id="Management2"]/div/div/div[1]/div/div[2]/form/div/div[3]/button').click()

t.sleep(2)
WebDriverWait(driver,10).until(lambda x: driver.find_elements_by_class_name("ant-menu-submenu-title")[1]).click()
WebDriverWait(driver,10).until(lambda x: driver.find_element_by_link_text("帐号管理")).click()

t.sleep(2)
WebDriverWait(driver,10).until(lambda x: driver.find_elements_by_class_name("ant-menu-item"))

#WebDriverWait(driver,10).until(lambda x: driver.find_elements_by_class_name("")[]).click()
WebDriverWait(driver,10).until(lambda x: driver.find_elements_by_class_name("ant-tree-title")[0]).click()