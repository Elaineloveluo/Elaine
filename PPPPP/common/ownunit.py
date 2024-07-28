import sys,unittest
from page.loginpage import LoginPage
sys.path.append('../basepase')
sys.path.append('../page')
from selenium import webdriver


class MyunitTests(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.testin.cn/account/login.htm'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.loginpage = LoginPage(self.url,self.driver)

    def tearDown(self):
        self.driver.quit()