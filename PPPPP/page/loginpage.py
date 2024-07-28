import sys,time
sys.path.append('../basepase')
from basepase.homeBage import HomePage    #导入HomePage基础类
from page.loginby import LoginBy #定位方式
from time import sleep


class LoginPage(HomePage,LoginBy):
    # 打开登录页面
    def openLoginPage(self):
        self.driver.get(self.url)
        self.driver.refresh()
        self.driver.maximize_window()
        sleep(0.5)

    # 输入用户名
    def input_userName(self, userName):
        self.find_element(*self.username_loc).send_keys(userName)

    # 输入密码
    def input_passWord(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    # 点击“登录”按钮
    def click_loginBtn(self):
        self.find_element(*self.loginBtn_loc).click()

    # 获取登录成功后的提示信息
    def get_assertText(self):
        return self.find_element(*self.logoutBtn_loc).text

    # 用户名为空的提示
    def get_userNullText(self):
        return self.find_element(*self.userNull_loc).text

    # 密码为空的提示
    def get_passwordNullText(self):
        return self.find_element(*self.passWordNull_loc).text

    # 登录成功后关闭弹框
    def get_tankuangclick(self):
        return self.find_element(*self.tankuang_loc).click()

    # bug管理点击
    def get_bugguanli_loc(self):
        return self.find_element(*self.bugguanli_loc).click()

    # bug管理页面核对
    def get_bugguanlitext_loc(self):
        return self.find_element(*self.bugguanlitext_loc).text

    # bug新建点击
    def get_bugxinjian_loc(self):
        return self.find_element(*self.bugxinjian_loc).click()

    # bug新建页面核对
    def get_bugxinjiantext_loc(self):
        return self.find_element(*self.bugxinjiantext_loc).text

    # bug进行中点击
    def get_bugjinxingzhong_loc(self):
        return self.find_element(*self.bugjinxingzhong_loc).click()

    # bug进行中页面核对
    def get_bugjinxingzhongtext(self):
        return self.find_element(*self.bugjinxingzhongtext_loc).text

    # bug已解决点击
    def get_bugyijiejue_loc(self):
        return self.find_element(*self.bugyijiejue_loc).click()

    # bug已解决页面核对
    def get_bugyijiejuetext_loc(self):
        return self.find_element(*self.bugyijiejuetext_loc).text

    # bug延期处理点击
    def get_bugyanqichuli_loc(self):
        return self.find_element(*self.bugyanqichuli_loc).click()

    # bug延期处理页面核对
    def get_bugyanqichulitext_loc(self):
        return self.find_element(*self.bugyanqichulitext_loc).text

    # bug重新打开点击
    def get_bugchongxindakai_loc(self):
        return self.find_element(*self.bugchongxindakai_loc).click()

    # bug重新打开页面核对
    def get_bugchongxindakaitext_loc(self):
        return self.find_element(*self.bugchongxindakaitext_loc).text

    # bug已验收点击
    def get_bugyiyanshou_loc(self):
        return self.find_element(*self.bugyiyanshou_loc).click()

    # bug已验收页面核对
    def get_bugyiyanshoutext_loc(self):
        return self.find_element(*self.bugyiyanshoutext_loc).text

    # bug已拒绝点击
    def get_bugyijujue_loc(self):
        return self.find_element(*self.bugyijujue_loc).click()

    # bug已拒绝页面核对
    def get_bugyijujuetext_loc(self):
        return self.find_element(*self.bugyijujuetext_loc).text

    # 项目总览点击
    def get_xinagmuclick_loc(self):
        return self.find_element(*self.xinagmuclick_loc).click()

    # 项目总览页面核对
    def get_xiangmuok_loc(self):
        return self.find_element(*self.xiangmuok_loc).text

    # 真机点击
    def get_zhenjiclick_loc(self):
        return self.find_element(*self.zhenjiclick_loc).click()

    # 真机页面核对
    def get_zhenjiok_loc(self):
        return self.find_element(*self.zhenjiok_loc).text

    # 兼容性点击
    def get_jianrongxingclick_loc(self):
        return self.find_element(*self.jianrongxingclick_loc).click()

    # 兼容性页面核对
    def get_jianrongxingok_loc(self):
        return self.find_element(*self.jianrongxingok_loc).text

    # 测试管理点击
    def get_ceshiguanli_loc(self):
        return self.find_element(*self.ceshiguanli_loc).click()

    # 应用管理点击
    def get_yingyongguanli_loc(self):
        return self.find_element(*self.yingyongguanli_loc).click()

    # 应用管理页面核对
    def get_yingyongguanlitext_loc(self):
        return self.find_element(*self.yingyongguanlitext_loc).text

    # 用例管理点击
    def get_yongliguanli_loc(self):
        return self.find_element(*self.yongliguanli_loc).click()

    # 用例管理页面核对
    def get_yongliguanlitext_loc(self):
        return self.find_element(*self.yongliguanlitext_loc).text

    # 测试计划点击
    def get_ceshijihua_loc(self):
        return self.find_element(*self.ceshijihua_loc).click()

    # 测试计划页面核对
    def get_ceshijihuatext_loc(self):
        return self.find_element(*self.ceshijihuatext_loc).text

    # 项目管理点击
    def get_xiangmuguanli_loc(self):
        return self.find_element(*self.xiangmuguanli_loc).click()

    # 项目管理页面核对
    def get_xiangmuguanlitext_loc(self):
        return self.find_element(*self.xiangmuguanlitext_loc).text

    # 组装成登录流程
    def login_gjs_pro(self, username, password):
        self.input_userName(username)
        self.input_passWord(password)
        self.click_loginBtn()
