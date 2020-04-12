from selenium import webdriver
from pages.add_student_info_page import AddStudentInfo, home_url
from pages.login_page import Login, login_url
import unittest
import time

class TestAddStudentInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(login_url)
        # 先登录
        a = Login(cls.driver)
        a.login()  # 先登录

        cls.student = AddStudentInfo(cls.driver)
        cls.student.gengduo()  # 先进更多   起点

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        # 让用例回到操作的起点位置
        self.driver.get(home_url)

    def test_add_01(self):
        '''登录-添加学生信息-成功案例: 测试数据， 200002，张三xxx '''
        s_id = str(time.time())  # int
        self.student.add_sudent(s_id, "张三xxx")
        # result = self.student.is_add_student_sucess("200001")
        # print("结果：%s" % result)
        r2 = self.student.is_add_sucess(s_id)
        print("实际结果：%s" % str(r2))
        self.assertTrue(r2)

    def test_add_02(self):
        '''登录-添加学生信息-无法提交: 测试数据，缺少id'''
        self.student.add_student_id("张三")
        time.sleep(3)
        loc_x = ("css selector", ".default.btn.btn-primary.hide-xs")
        # 实际结果
        result = self.student.is_element_exist(loc_x)
        print("实际结果：%s" % result)
        # 期望结果
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
