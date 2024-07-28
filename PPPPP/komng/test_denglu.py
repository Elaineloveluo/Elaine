import sys,unittest
import time

sys.path.append('../basepase')
sys.path.append('../page')
from page.loginpage import LoginPage
from common.ownunit import MyunitTests
from common.helper import Helper
from common.getimage import SavaImage
from common.log import GetLog
import logging


class Test_Denglu(MyunitTests,LoginPage,Helper,GetLog):
    def test_dengluok(self):
        #正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1),self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(),self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        SavaImage(self.driver,'login_success.png')
        self.makelog('PO-gjs:登录成功后获取截图信息')
        self.makelog('PO-gjs:第一条用例执行结束。。。。。。')
    #
    # def test_password_null(self):
    #     #测试密码为空
    #     self.loginpage.openLoginPage()
    #     self.makelog('PO-gjs:打开浏览器进入到项目首页')
    #     self.loginpage.login_gjs_pro(self.readusername(2),self.readpassword(2))
    #     self.makelog('PO-gjs:输入正确的用户名和密码为空')
    #     self.assertEqual(self.loginpage.get_passwordNullText(),self.exceptText(2))
    #     self.makelog('PO-gjs:登录失败获取信息进行断言')
    #     SavaImage(self.driver, 'login_password_null.png')
    #     self.makelog('PO-gjs:登录失败后获取截图信息')
    #     self.makelog('PO-gjs:第二条用例执行结束。。。。。。')
    #
    # def test_user_null(self):
    #     #测试用户为空
    #     self.loginpage.openLoginPage()
    #     self.makelog('PO-gjs:打开浏览器进入到项目首页')
    #     self.loginpage.login_gjs_pro(self.readusername(3),self.readpassword(3))
    #     self.makelog('PO-gjs:输入用户名为空和正确密码')
    #     self.assertEqual(self.loginpage.get_userNullText(),self.exceptText(3))
    #     self.makelog('PO-gjs:登录失败获取信息进行断言')
    #     SavaImage(self.driver, 'login_user_null.png')
    #     self.makelog('PO-gjs:登录失败后获取截图信息')
    #     self.makelog('PO-gjs:第三条用例执行结束。。。。。。')
    #
    # def test_user_password_null(self):
    #     #测试用户/密码都为空
    #     self.loginpage.openLoginPage()
    #     self.makelog('PO-gjs:打开浏览器进入到项目首页')
    #     self.loginpage.login_gjs_pro(self.readusername(4),self.readpassword(4))
    #     self.makelog('PO-gjs:输入用户名和密码为空')
    #     self.assertEqual(self.loginpage.get_userNullText(),self.exceptText(4))
    #     self.makelog('PO-gjs:登录失败获取信息进行断言')
    #     SavaImage(self.driver, 'login_user_null.png')
    #     self.makelog('PO-gjs:登录失败后获取截图信息')
    #     self.makelog('PO-gjs:第四条用例执行结束。。。。。。')


if __name__ == '__main__':
    unittest.main(verbosity=2)