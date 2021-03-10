from base.basePage import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from pywinauto import application
from ext_method.findFileByDate import *
import time as t


class management_updateapp(WebDriver):
    update_page = (By.CLASS_NAME,'item-title')
    update_app = (By.CLASS_NAME, 'upload-box')
    submit_app = (By.CLASS_NAME,'ant-btn.ant-btn-primary')
    submit_app1 = (By.XPATH,'//div[6]//button[@class="ant-btn ant-btn-primary"]')
    submit_app2 = (By.XPATH,'//div[7]//button[@class="ant-btn ant-btn-primary"]')
    update_error_loc=(By.CLASS_NAME,'ant-message-notice')

    #进入“客户端更新”
    @property
    def clickupdatepage(self):
        self.findElements(*self.update_page)[2].click()

    #确认创建策略
    def updatesubmit(self,order):
        '''
        # 选择策略，不能使用Select类处理
        WebDriverWait(driver, 30).until(lambda x: driver.find_element_by_class_name("ant-select-arrow")).click()
        WebDriverWait(driver, 30).until(
            lambda x: driver.find_elements_by_class_name("ant-select-dropdown-menu-item")[-1]).click()
        '''
        try:
            self.findElement(*self.submit_app).click()
        except:
            try:
                self.findElement(*self.submit_app1).click()
            except:
                self.findElement(*self.submit_app2).click()
        #btn=self.findElementForLongTime(*self.submit_app)
        #btn="document.getElementsByClassName('ant-btn.ant-btn-primary')[0].click()"
        #self.driver.execute_script("arguments["+str(int(order))+"].click();",btn)

    #上传安装包
    def clickupdateapp(self,order,path):#order:0pc;1ios;2android
        self.findElements(*self.update_app)[int(order)].click()
        self.find_appfile(path)
        t.sleep(3)
        self.updatesubmit(order)
        t.sleep(2)#操作提示默认显示3秒

    #选择对应app文件中最新文件
    def find_appfile(self,path):
        t.sleep(1)
        app = application.Application()
        window = app.connect(title_re=u"打开")
        window["Dialog"]["Edit"].type_keys(FindFileByDate().find_file(path))
        window["Dialog"][u"打开(O)"].click()

    #获取策略确认后提示文案
    @property
    def updateError(self):
        return self.findElements(*self.update_error_loc)[-1].text
