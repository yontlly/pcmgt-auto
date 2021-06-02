from base.basePage import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from pywinauto import application
import time as t
from selenium.webdriver.common.keys import Keys


class Account(WebDriver):
    #从首页到账户管理页面
    account_center = (By.CLASS_NAME,'ant-menu-submenu-title')
    account_management = (By.LINK_TEXT,u"帐号管理")

    #选择组织树
    tree_root=(By.CLASS_NAME,'ant-tree-title')#组织树根
    tree_under=(By.CLASS_NAME,'ant-tree-title')

    #部门的增删改元素
    add_dept=(By.CLASS_NAME,'ant-btn.addpart.ant-btn-primary')#添加子部门
    add_dept_name=(By.CLASS_NAME,'ant-input.departinput')#部门名称
    created_dept_group=(By.CLASS_NAME,'ant-checkbox.ant-checkbox-checked')#已勾选创建部门群
    update_dept=(By.CLASS_NAME,'ant-btn.setname.ant-btn-primary')
    delete_dept=(By.CLASS_NAME,'ant-btn.deletepart.ant-btn-primary')
    # 创建部门群
    #add_dept_group=(By.CLASS_NAME,'ant-checkbox-input')
    add_dept_group=(By.XPATH,'//div[contains(@class,"ant-modal-content")]//input[contains(@class,"ant-checkbox-input")]')
    # 添加部门确定
    #add_dept_submit=(By.CLASS_NAME,'ant-btn-primary')#添加部门确定
    add_dept_submit=(By.XPATH,'//button[contains(@class,"ant-btn ant-btn-primary")]')

    #确定删除按钮
    delete_sure_submit=(By.XPATH,'//button[contains(@class,"ant-btn ant-btn-danger")]')


    add_user=(By.CLASS_NAME,'ant-btn.btnadd.ant-btn-primary')
    move_user=(By.CLASS_NAME,'ant-btn.btnsetpart.ant-btn-primary')
    update_order=(By.CLASS_NAME,'ant-btn.btnorder.ant-btn-primary')
    delete_user=(By.CLASS_NAME,'ant-btn.btndel.ant-btn-primary')
    stop_user=(By.CLASS_NAME,'ant-btn.btnstop.ant-btn-primary')
    update_user=()


    userinfo=(By.CLASS_NAME,'ant-input')#索引0为搜索框;1姓名;5邮箱
    userpassword=(By.ID,'pwd')
    userinfo_has=(By.CLASS_NAME,'ant-form-item-control.has-success')#has-success表示成员信息中已有值
    user_submit1=(By.XPATH,'//*[@id="Memadd"]//button[@class="ant-btn ant-btn-primary"][1]')#保存继续添加
    user_submit2=(By.XPATH,'//*[@id="Memadd"]//button[@class="ant-btn ant-btn-primary"][2]')#保存
    userlist=(By.CLASS_NAME,'limember')

    #编辑成员按钮
    edit_user_back=(By.XPATH,'//div[@class="detail"]//button[@class="ant-btn"][1]')
    edit_user_submit=(By.XPATH,'//div[@class="detail"]//button[@class="ant-btn ant-btn-primary"]')
    edit_user_stop=(By.XPATH,'//div[@class="detail"]//button[@class="ant-btn"][2]')
    edit_user_delete=(By.XPATH,'//div[@class="detail"]//button[@class="ant-btn dsave ant-btn-danger"]')

    #人员前的checkbox
    userlist_choose=(By.XPATH,'//*[@id="ManaTable"]//span[@class="ant-checkbox-inner"]')#定位部门中的第一个人

    operating_hints_loc = (By.CLASS_NAME, 'ant-message-notice')#操作提示

    @property
    def gotoAccountMgt(self):
        self.findElements(*self.account_center)[1].click()
        self.findElement(*self.account_management).click()

    @property
    def button_submit(self):
        btn=self.findElement(*self.add_dept_submit)
        self.driver.execute_script("arguments[0].click();",btn)

    def addDept(self,name):
        self.findElements(*self.tree_root)[0].click()
        self.findElement(*self.add_dept).click()
        self.findElement(*self.add_dept_name).send_keys(name)
        t.sleep(2)
        # try:
        #     self.findElement(*self.created_dept_group)
        # except:
        #     self.findElement(*self.add_dept_group).click()
        self.findElement(*self.add_dept_submit).click()

    def editDept(self,name):
        self.findElements(*self.tree_under)[-1].click()
        self.findElement(*self.update_dept).click()
        self.findElement(*self.add_dept_name).send_keys(name)
        self.findElement(*self.add_dept_submit).click()

    def addUser(self,name):
        self.findElements(*self.tree_under)[-1].click()
        self.findElement(*self.add_user).click()
        num = 2
        for i in range(num):
            t.sleep(2)
            self.findElements(*self.userinfo)[1].send_keys(name+str(i))
            self.findElements(*self.userinfo)[5].send_keys("123@qq.com")
            self.findElement(*self.userpassword).send_keys("11111111")
            if num-1 == i:
                self.findElement(*self.user_submit2).click()
            else:
                self.findElement(*self.user_submit1).click()

    def editUser(self,name):
        self.findElements(*self.userlist)[-1].click()
        t.sleep(2)
        self.findElements(*self.userinfo)[1].send_keys(Keys.CONTROL,'a')
        self.findElements(*self.userinfo)[1].send_keys(name)
        self.findElement(*self.edit_user_submit).click()

    # def stopUser_one(self):
    #     self.findElements(*self.userlist_choose)[0].click()
    #     self.findElement(*self.stop_user).click()
    #     t.sleep(2)
    #     self.findElement(*self.add_dept_submit).click()

    def deleteUser_two(self):
        self.findElements(*self.userlist_choose)[0].click()
        self.findElement(*self.delete_user).click()
        t.sleep(2)
        self.findElement(*self.delete_sure_submit).click()

    def deleteUser_one(self):#详情中删除
        self.findElements(*self.userlist)[-1].click()
        t.sleep(2)
        self.findElement(*self.edit_user_delete).click()
        t.sleep(2)
        self.findElements(*self.add_dept_submit)[1].click()#此时界面上存在2个确认

    def deleteDept(self):
        self.findElements(*self.tree_under)[-1].click()
        self.findElement(*self.delete_dept).click()
        self.findElement(*self.add_dept_submit).click()

    @property
    def operatingHints(self):
        return self.findElements(*self.operating_hints_loc)[-1].text

