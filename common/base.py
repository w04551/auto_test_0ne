from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

'''
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
'''

class Base():

    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver

    def find(self, locator):
        '''loctor = ("id", "kw")'''
        element = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*locator))
        return element

    def findx(self, locator):
        element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(locator))
        return element

    def finds(self, locator):
        '''loctor = ("id", "kw")'''
        elements = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_elements(*locator))
        return elements

    def send(self, locator, text):
        '''loctor = ("id", "kw")'''
        self.find(locator).send_keys(text)

    def click(self, locator):
        '''点击元素'''
        self.find(locator).click()

    def clear(self, locator):
        self.find(locator).clear()

    def is_element_exist(self, locator):
        '''判断元素是否存在'''
        try:
            self.find(locator)
            return True
        except:
            return False

    def text_in_element(self, locator, _text):
        '''判断元素text属性'''
        try:
            r = WebDriverWait(self.driver, 30, 1).until(EC.text_to_be_present_in_element(locator, _text))
            return r
        except:
            return False

    def value_in_element(self, locator, _text):
        '''判断元素value属性'''
        try:
             r = WebDriverWait(self.driver, 30, 1).until(EC.text_to_be_present_in_element_value(locator, _text))
             return r
        except:
             return False

    def get_text(self, locator):
        '''获取元素文本值'''
        try:
            t = self.find(locator).text
        except:
            t = ""
        return t

    def move_to_element(self, locator):
        '''鼠标悬停'''
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def select_by_index(self, locator, index=0):
        '''select下拉框， index索引'''
        element = self.find(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        element = self.find(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, _text):
        element = self.find(locator)
        Select(element).select_by_value(_text)

    def is_alert(self, timeout=3):
        '''
        判断是否有alert, 没有返回false, 有返回alert对象
        :param timeout:
        :return:
        '''
        try:
            alert = WebDriverWait(self.driver, timeout, 1).until(EC.alert_is_present())
            return alert
        except:
            return False

    def js_focus_element(self,locator):
        '''聚焦元素'''
        target = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
       '''滚动到顶部'''
       js = "window.scrollTo(0,0)"
       self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = (0, "document.body.scrollHeight")
        self.driver.execute_script(js)





if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1/zentao/user-login.html")

    from selenium.webdriver.common.by import By

    # driver.find_element(By.ID, "id值")
    # driver.find_element("id", "id值")


    b = Base(driver)
    # 登录
    loc1 = ("css selector", "#account")
    b.send(loc1, "admin")

    loc2 = ("css selector", "[name='password']")
    b.send(loc2, "123456")

    loc3 = ("css selector", "#submit")
    b.click(loc3)






