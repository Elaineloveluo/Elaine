import sys,unittest
sys.path.append('../basepase')
sys.path.append('../page')
from page.loginpage import LoginPage
from common.ownunit import MyunitTests
from common.helper import Helper
from common.getimage import SavaImage
from common.log import GetLog


class Test_Bugguanli(MyunitTests,LoginPage,Helper,GetLog):
    def test_bugclick(self):
        #正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1),self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(),self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_bugguanli_loc()
        self.makelog('PO-gjs:bug管理点击完成')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.makelog('PO-gjs:定位bug管理跳转的新页面')
        self.assertEqual('与我相关缺陷',self.loginpage.get_bugguanlitext_loc())
        self.makelog('PO-gjs:bug管理点击核对完成')
        SavaImage(self.driver, 'bugguanli.png')
        self.makelog('PO-gjs:第一条用例执行结束。。。。。。')

    def test_xinjian(self):
        # 正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_bugguanli_loc()
        self.makelog('PO-gjs:bug管理点击完成')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.makelog('PO-gjs:定位bug管理跳转的新页面')
        self.loginpage.get_bugxinjian_loc()
        self.makelog('PO-gjs:bug新建点击完成')
        self.assertEqual('问题状态：新建',self.loginpage.get_bugxinjiantext_loc())
        SavaImage(self.driver, 'bugxinjian.png')
        self.makelog('PO-gjs:第二条用例执行结束。。。。。。')

    def test_jinxing(self):
        # 正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_bugguanli_loc()
        self.makelog('PO-gjs:bug管理点击完成')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.makelog('PO-gjs:定位bug管理跳转的新页面')
        self.loginpage.get_bugjinxingzhong_loc()
        self.makelog('PO-gjs:bug进行中点击完成')
        self.assertEqual('问题状态：进行中',self.loginpage.get_bugjinxingzhongtext())
        SavaImage(self.driver, 'bugjinxing.png')
        self.makelog('PO-gjs:第三条用例执行结束。。。。。。')

    def test_yijiejue(self):
        # 正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_bugguanli_loc()
        self.makelog('PO-gjs:bug管理点击完成')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.makelog('PO-gjs:定位bug管理跳转的新页面')
        self.loginpage.get_bugyijiejue_loc()
        self.makelog('PO-gjs:bug已解决点击完成')
        self.assertEqual('问题状态：已解决', self.loginpage.get_bugyijiejuetext_loc())
        SavaImage(self.driver, 'bugyijiejue.png')
        self.makelog('PO-gjs:第四条用例执行结束。。。。。。')

    def test_yanqichuli(self):
        # 正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_bugguanli_loc()
        self.makelog('PO-gjs:bug管理点击完成')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.makelog('PO-gjs:定位bug管理跳转的新页面')
        self.loginpage.get_bugyanqichuli_loc()
        self.makelog('PO-gjs:bug延期处理点击完成')
        self.assertEqual('问题状态：延期处理', self.loginpage.get_bugyanqichulitext_loc())
        SavaImage(self.driver, 'bugyanqichuli.png')
        self.makelog('PO-gjs:第五条用例执行结束。。。。。。')

    def test_chongxindakai(self):
        # 正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_bugguanli_loc()
        self.makelog('PO-gjs:bug管理点击完成')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.makelog('PO-gjs:定位bug管理跳转的新页面')
        self.loginpage.get_bugchongxindakai_loc()
        self.makelog('PO-gjs:bug重新打开点击完成')
        self.assertEqual('问题状态：重新打开', self.loginpage.get_bugchongxindakaitext_loc())
        SavaImage(self.driver, 'bugchongxindakai.png')
        self.makelog('PO-gjs:第六条用例执行结束。。。。。。')

    def test_yiyanshou(self):
        # 正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_bugguanli_loc()
        self.makelog('PO-gjs:bug管理点击完成')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.makelog('PO-gjs:定位bug管理跳转的新页面')
        self.loginpage.get_bugyiyanshou_loc()
        self.makelog('PO-gjs:bug已验收点击完成')
        self.assertEqual('问题状态：已验收', self.loginpage.get_bugyiyanshoutext_loc())
        SavaImage(self.driver, 'bugyiyanshou.png')
        self.makelog('PO-gjs:第七条用例执行结束。。。。。。')

    def test_yijujue(self):
        # 正确的用户名和密码
        self.loginpage.openLoginPage()
        self.makelog('PO-gjs:打开浏览器进入到项目首页')
        self.loginpage.login_gjs_pro(self.readusername(1), self.readpassword(1))
        self.makelog('PO-gjs:输入正确的用户名和密码')
        self.assertEqual(self.loginpage.get_assertText(), self.exceptText(1))
        self.makelog('PO-gjs:登录成功获取信息进行断言')
        self.loginpage.get_tankuangclick()
        self.makelog('PO-gjs:登录成功后的弹框已关闭')
        self.loginpage.get_bugguanli_loc()
        self.makelog('PO-gjs:bug管理点击完成')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.makelog('PO-gjs:定位bug管理跳转的新页面')
        self.loginpage.get_bugyijujue_loc()
        self.makelog('PO-gjs:bug已拒绝点击完成')
        self.assertEqual('问题状态：已拒绝', self.loginpage.get_bugyijujuetext_loc())
        SavaImage(self.driver, 'bugyijujue.png')
        self.makelog('PO-gjs:第八条用例执行结束。。。。。。')


if __name__ == '__main__':
    unittest.main(verbosity=2)