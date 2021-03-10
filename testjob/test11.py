import time as t
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.expected_conditions import NoSuchElementException


chrome_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
driver= webdriver.Chrome(executable_path=chrome_path)
driver.get('http://10.206.104.220:8787/pc-management/#/login')
#driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id('userName').send_keys('123123')
driver.find_element_by_id('password').send_keys('123123')
driver.find_element_by_xpath('//*[@id="Management2"]/div/div/div[1]/div/div[2]/form/div/div[3]/button').click()

# try:
#     wait.until(lambda x: driver.find_element_by_xpath('/html/body/div[3]/div/span/div'))
#     print(driver.find_element_by_xpath('/html/body/div[3]/div/span/div').text)
# except NoSuchElementException as e:
#     wait.until(lambda x: driver.find_elements_by_class_name("ant-form-explain")[0])
#     print(driver.find_elements_by_class_name('ant-form-explain')[0].text)
try:
    wait = ui.WebDriverWait(driver, 5)
    wait.until(lambda x: driver.find_elements_by_class_name('ant-form-explain')[0])
    print(driver.find_elements_by_class_name('ant-form-explain')[0].text)
except:
    wait = ui.WebDriverWait(driver, 5)
    wait.until(lambda x: driver.find_element_by_xpath("/html/body/div[3]/div/span/div"))
    print(driver.find_element_by_xpath('/html/body/div[3]/div/span/div').text)
driver.quit()