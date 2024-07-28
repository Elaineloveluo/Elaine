import sys,unittest
sys.path.append('../basepase')
sys.path.append('../page')
from page.loginpage import LoginPage
from common.ownunit import MyunitTests
from common.helper import Helper
from common.getimage import SavaImage
from common.log import GetLog


class Test_Ceshiguanli(MyunitTests,LoginPage,Helper,GetLog):
    def test_yingyong(self):
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_ceshiguanli_loc()
        self.makelog('PO-gjs:测试管理已点击')
        self.loginpage.get_yingyongguanli_loc()
        self.makelog('PO-gjs:应用管理已点击')
        self.assertEqual('应用管理',self.loginpage.get_yingyongguanlitext_loc())
        self.makelog('PO-gjs:应用管理页面核对准确')
        SavaImage(self.driver, 'yingyongyemian.png')
        self.makelog('PO-gjs:第一条用例执行结束。。。。。。')

    def test_yongli(self):
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_ceshiguanli_loc()
        self.makelog('PO-gjs:测试管理已点击')
        self.loginpage.get_yongliguanli_loc()
        self.makelog('PO-gjs:用例管理已点击')
        self.assertEqual('用例管理',self.loginpage.get_yongliguanlitext_loc())
        self.makelog('PO-gjs:用例管理页面核对准确')
        SavaImage(self.driver, 'yongliyemian.png')
        self.makelog('PO-gjs:第二条用例执行结束。。。。。。')

    def test_jihua(self):
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_ceshiguanli_loc()
        self.makelog('PO-gjs:测试管理已点击')
        self.loginpage.get_ceshijihua_loc()
        self.makelog('PO-gjs:测试计划已点击')
        self.assertEqual('测试计划',self.loginpage.get_ceshijihuatext_loc())
        self.makelog('PO-gjs:测试计划页面核对准确')
        SavaImage(self.driver, 'jihuayemian.png')
        self.makelog('PO-gjs:第三条用例执行结束。。。。。。')

    def test_xiangmu(self):
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_ceshiguanli_loc()
        self.makelog('PO-gjs:测试管理已点击')
        self.loginpage.get_xiangmuguanli_loc()
        self.makelog('PO-gjs:项目管理已点击')
        self.assertEqual('项目管理',self.loginpage.get_xiangmuguanlitext_loc())
        self.makelog('PO-gjs:项目管理页面核对准确')
        SavaImage(self.driver, 'xiangmuyemian.png')
        self.makelog('PO-gjs:第四条用例执行结束。。。。。。')


if __name__ == '__main__':
    unittest.main(verbosity=2)



