'''
目标  场景：登录-添加学生信息-判断添加成功
1.登录
- 输入账号
- 输入密码
- 点登陆

2.添加
- 更多
- 点左侧 学生
- 点添加按钮
- 输入页面 （ 学生信息录入)
- 点提交

3.判断是否添加成功
- 页面跳转到列表页
- 判断： 新提交的学生信息在当前列表页
'''

from common.base import Base
from pages.login_page import Login

home_url = "http://47.104.190.48:8000/xadmin/"


class AddStudentInfo(Base):
    loc1 = ("link text", "进主页更多功能")   # 更多
    loc2 = ("xpath", '//*[@id="left-side"]/ul[1]/li[7]/a')  # 学生
    loc3 = ("xpath", '//*[@id="content-block"]/div[1]/div[2]/div/a')  # 添加学生
    loc4 = ("name", "student_id")
    loc5 = ("name", "name")
    # 先点下
    loc6 = ("xpath", '//*[@id="div_id_gender"]/div/div/div[1]')
    # 选择选项
    loc7 = ("xpath", ".//*[@id='div_id_gender']/div/div/div[2]/div/div[2]")
    loc8 = ("name", "age")
    loc9 = ("xpath", ".//*[@id='student_form']/div[2]/button")

    loc_r = ("xpath", ".//*[@id='changelist-form']/div[1]/table/tbody/tr[1]/td[2]")

    def gengduo(self):
        self.click(self.loc1)

    def add_sudent(self, s_id, s_name):
        '''正常流程'''
        self.click(self.loc2)
        self.click(self.loc3)
        self.send(self.loc4, s_id)
        self.send(self.loc5, s_name)
        self.click(self.loc6)
        self.click(self.loc7)
        self.send(self.loc8, "11")
        self.click(self.loc9)

    def add_student_id(self, s_name):
        '''输入参数缺少id'''
        self.click(self.loc2)
        self.click(self.loc3)
        # self.send(self.loc4, s_id)
        self.send(self.loc5, s_name)
        self.click(self.loc6)
        self.click(self.loc7)
        self.send(self.loc8, "11")
        self.click(self.loc9)


    def is_add_student_sucess(self, text):
        # 判断 text  "学生名称" 在列表里 包含
        # "学生名称" 在 当前页面
        # t = self.driver.page_source
        body = ("tag name", "body")
        t2 = self.find(body).text
        # print(t2)
        return text in t2

    def is_add_sucess(self, s_id):
        t = self.get_text(self.loc_r)
        print("获取的学号：%s" % t)
        return s_id in t

if __name__ == '__main__':
    # 必须调试代码，自测
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get("http://47.104.190.48:8000/login")
    a = Login(driver)
    a.login()  # 先登录
    b = AddStudentInfo(driver)
    b.add_sudent("200002", "张三xxx")
    result = b.is_add_student_sucess("200001")
    print("结果：%s" % result)
    r2 = b.is_add_sucess("200002")
    print(r2)






