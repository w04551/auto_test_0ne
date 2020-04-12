from common.base import Base

login_url = "http://47.104.190.48:8000/login"


class Login(Base):
    loc1 = ("id", "id_username")
    loc2 = ("id", "id_password")
    loc3 = ("xpath", '//*[@value="确定"]')
    login_xpath = ("xpath", '//*[@id="top-nav"]/div[2]/ul/li[2]/a/strong')

    def login(self, user="testyoyo", psw="123456"):
        self.send(self.loc1, user)
        self.send(self.loc2, psw)
        self.click(self.loc3)

if __name__ == '__main__':
    # 必须调试代码，自测
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get("http://47.104.190.48:8000/login")
    loginpage = Login(driver)
    loginpage.login()