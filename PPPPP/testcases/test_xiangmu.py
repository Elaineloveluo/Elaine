import sys,unittest
sys.path.append('../basepase')
sys.path.append('../page')
from page.loginpage import LoginPage
from common.ownunit import MyunitTests
from common.helper import Helper
from common.getimage import SavaImage
from common.log import GetLog


class Test_Xiangmu(MyunitTests,LoginPage,Helper,GetLog):
    def test_xiangmuzonglan(self):
        #正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1),self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(),self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_xinagmuclick_loc()
        self.makelog('PO-gjs:项目总览点击完成')
        self.assertEqual('任务动态',self.get_xiangmuok_loc())
        self.makelog('PO-gjs:项目总览点击核对完成')
        SavaImage(self.driver, 'xiangmuzonglan.png')
        self.makelog('PO-gjs:第一条用例执行结束。。。。。。')
'''
    def test_yuanchengzhenji(self):
        #正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1),self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(),self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_zhenjiclick_loc()
        self.makelog('PO-gjs:远程真机点击完成')
        self.assertEqual('远程真机',self.get_zhenjiok_loc())
        self.makelog('PO-gjs:远程真机点击核对完成')
        SavaImage(self.driver, 'yuanchengzhenji.png')
        self.makelog('PO-gjs:第二条用例执行结束。。。。。。')

    def test_biaozhunjianrongceshi(self):
        #正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1),self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(),self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_jianrongxingclick_loc()
        self.makelog('PO-gjs:标准兼容测试点击完成')
        self.assertEqual('标准兼容测试',self.get_jianrongxingok_loc())
        self.makelog('PO-gjs:标准兼容测试点击核对完成')
        SavaImage(self.driver, 'jianrongxing.png')
        self.makelog('PO-gjs:第三条用例执行结束。。。。。。')
'''

if __name__ == '__main__':
    unittest.main(verbosity=2)