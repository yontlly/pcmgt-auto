from base.basePage import *
from selenium.webdriver.common.by import By
from pywinauto import application
import time as t
import os


class CorpInfo(WebDriver):

    #从首页到组织管理页面
    menu = (By.CLASS_NAME,'ant-menu-submenu-title')
    corp_info = (By.LINK_TEXT,u"组织信息")

    #编辑/保存按钮
    edit=(By.CLASS_NAME,'ant-btn.ant-btn-primary')

    #编辑内容
    content=(By.XPATH,'//input[@class="ant-input input"]')#0组织名称1简称2组织地址3组织官网

    #上传/删除/取消编辑按钮
    import_delete_cencel=(By.CLASS_NAME,'ant-btn')#0上传1删除2取消编辑

    operating_hints_loc = (By.CLASS_NAME, 'ant-message-notice')#操作提示

    @property
    def gotoCorpinfo(self):
        self.findElements(*self.menu)[0].click()
        self.findElement(*self.corp_info).click()

    @property
    def editOrSave(self):
        self.findElement(*self.edit).click()

    def importPicture(self):
        self.findElements(*self.import_delete_cencel)[0].click()#点击上传
        t.sleep(3)
        self.find_picture()#图片上传过程

    def find_picture(self):
        app = application.Application()
        window = app.connect(title_re=u"打开")
        window["Dialog"]["Edit"].type_keys(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),'data','corpinfo.png'))
        window["Dialog"][u"打开(O)"].click()

    #编辑内容
    def editContent(self,*args):
        for arg in args:
            self.findElements(*self.content)[args.index(arg)].send_keys(arg)
        #self.findElements(*self.content)[0].send_keys(corpname)
        #self.findElements(*self.content)[1].send_keys(corpname_2)
        #self.findElements(*self.content)[2].send_keys(corpaddr)
        #self.findElements(*self.content)[3].send_keys(corpweb)

    def editCorpInfo(self,*args):
        self.editOrSave
        self.importPicture()
        self.editContent(*args)
        t.sleep(2)
        self.editOrSave

    @property
    def operatingHints(self):
        return self.findElements(*self.operating_hints_loc)[-1].text