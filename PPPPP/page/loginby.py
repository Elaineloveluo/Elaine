from selenium.webdriver.common.by import By  #定位方式


class LoginBy():
    #定位器
    #用户名
    username_loc = (By.ID,'email')
    #密码
    password_loc = (By.ID,'pwd')
    #立即登录按钮
    loginBtn_loc = (By.ID,'submitBtn')
    #退出连接
    logoutBtn_loc = (By.CSS_SELECTOR,'#bs-example-navbar-collapse-1 > ul.nav.navbar-nav.navbar-right > li:nth-child(7) > a > span')
    #用户名为空
    userNull_loc = (By.ID,'email_err')
    #密码为空
    passWordNull_loc = (By.CSS_SELECTOR,'#pwd_err')
    #登录成功关闭弹框
    tankuang_loc = (By.ID, "onesignal-slidedown-allow-button")
    #点击项目总览
    xinagmuclick_loc = (By.CSS_SELECTOR,'li:nth-child(1) .title')
    #项目总览页面核对
    xiangmuok_loc = (By.CSS_SELECTOR, ".create_task_title > b")
    #点击远程真机
    zhenjiclick_loc = (By.CSS_SELECTOR, 'li:nth-child(2) .title')
    #真机页面核对
    zhenjiok_loc = (By.CSS_SELECTOR, ".breadcrumb > li:nth-child(2)")
    #点击标准兼容性测试
    jianrongxingclick_loc = (By.CSS_SELECTOR, 'li:nth-child(3) .title')
    #兼容性页面核对
    jianrongxingok_loc = (By.CSS_SELECTOR, ".active:nth-child(2)")
    #bug管理
    bugguanli_loc = (By.CSS_SELECTOR, "li:nth-child(4) .title")
    #bug管理页面核对
    bugguanlitext_loc = (By.CSS_SELECTOR, ".introduce_cont > p")
    #bug新建
    bugxinjian_loc = (By.CSS_SELECTOR, ".flex-item:nth-child(1) > .ng-binding")
    #bug新建页面核对
    bugxinjiantext_loc = (By.CSS_SELECTOR, "ul:nth-child(3) > .ng-scope:nth-child(1) > .ng-binding")
    #bug进行中
    bugjinxingzhong_loc = (By.CSS_SELECTOR, ".flex-item:nth-child(2) > .ng-binding")
    #bug进行中页面核对
    bugjinxingzhongtext_loc = (By.CSS_SELECTOR, "ul:nth-child(3) > .ng-scope:nth-child(1) > .ng-binding")
    #bug已解决
    bugyijiejue_loc = (By.CSS_SELECTOR, ".flex-item:nth-child(3) > .ng-binding")
    #bug已解决页面核对
    bugyijiejuetext_loc = (By.CSS_SELECTOR, "ul:nth-child(3) > .ng-scope:nth-child(1) > .ng-binding")
    #bug延期处理
    bugyanqichuli_loc = (By.CSS_SELECTOR, ".flex-item:nth-child(4) > .ng-binding")
    #bug延期处理页面核对
    bugyanqichulitext_loc = (By.CSS_SELECTOR, "ul:nth-child(3) > .ng-scope:nth-child(1) > .ng-binding")
    #bug重新打开
    bugchongxindakai_loc = (By.CSS_SELECTOR, ".flex-item:nth-child(5) > .ng-binding")
    #bug重新打开页面核对
    bugchongxindakaitext_loc = (By.CSS_SELECTOR, "ul:nth-child(3) > .ng-scope:nth-child(1) > .ng-binding")
    #bug已验收
    bugyiyanshou_loc = (By.CSS_SELECTOR, ".flex-item:nth-child(6) > .ng-binding")
    #bug已验收页面核对
    bugyiyanshoutext_loc = (By.CSS_SELECTOR, "ul:nth-child(3) > .ng-scope:nth-child(1) > .ng-binding")
    #bug已拒绝
    bugyijujue_loc = (By.CSS_SELECTOR, ".flex-item:nth-child(7) > .ng-binding")
    #bug已拒绝页面核对
    bugyijujuetext_loc = (By.CSS_SELECTOR, "ul:nth-child(3) > .ng-scope:nth-child(1) > .ng-binding")
    #测试管理点击
    ceshiguanli_loc = (By.CSS_SELECTOR, "li:nth-child(5) .title")
    #应用管理点击
    yingyongguanli_loc = (By.LINK_TEXT, "应用管理")
    #应用管理页面核对
    yingyongguanlitext_loc = (By.CSS_SELECTOR, ".active:nth-child(3)")
    #用例管理点击
    yongliguanli_loc = (By.LINK_TEXT, "用例管理")
    #用例管理页面核对
    yongliguanlitext_loc = (By.CSS_SELECTOR, ".breadcrumb > .active")
    #测试计划点击
    ceshijihua_loc = (By.LINK_TEXT, "测试计划")
    #测试计划页面核对
    ceshijihuatext_loc = (By.CSS_SELECTOR, ".breadcrumb > .active")
    #项目管理点击
    xiangmuguanli_loc = (By.LINK_TEXT, "项目管理")
    #项目管理页面核对
    xiangmuguanlitext_loc = (By.CSS_SELECTOR, ".active:nth-child(2)")


