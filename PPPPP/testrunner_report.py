#!/use/bin/env python
# coding:utf-8
import os,unittest,smtplib,time
from email.mime.text import MIMEText
from common.log import GetLog
from email.mime.multipart import MIMEMultipart
from unittestreport import TestRunner


class Runner(GetLog):
    def getSuite(self):
        '''获取要执行的测试套件'''
        suite = unittest.TestLoader().discover(
            start_dir=os.path.join((os.path.dirname(__file__)), 'testcases'),
            pattern='test_*.py',
            top_level_dir=None)
        return suite

    def send_mail(self, to_user, sub, content):
        '''
		发送邮件内容
		:param to_user:发送邮件的人
		:param sub:主题
		:param content:邮件内容
		'''
        global send_mail
        global send_user
        send_mail = send_mail_1
        send_user = send_user_1
        message = MIMEText(content, _subtype='plain', _charset='utf-8')  # 创建一个实例，这里设置为html格式邮件
        message['Subject'] = sub  # 设置主题
        message['From'] = send_user
        message['To'] = to_user
        server = smtplib.SMTP()
        server.connect(send_mail)  # 连接smtp服务器
        server.login('hbqfighting@163.com', 'hbq19941120')  # 登陆服务器
        server.sendmail(send_user, to_user, message.as_string())  # 发送邮件
        server.close()

    def run_case(self, getSuite, reportName="report"):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        print("项目目录：",base_dir)
        now = time.strftime("%Y%m%d-%H%M%S")
        test_dir = os.path.join(base_dir, 'testcases')  # 获取当前用例路径
        print("用例路径:", test_dir)  # 打印用例路径
        report_path = os.path.join(base_dir, reportName)  # 获取当前报告路径
        print("报告目录：",report_path)
        if not os.path.exists('report'):
            os.mkdir('report')
        report_name = f"Test_runner{now}.html"  # 报告后面加当前时间
        print("报告名称：",report_name)
        file_name = os.path.join(report_path,"Test_runner" + now + '.html')
        print("报告地址：",file_name)
        fp = open(file_name, 'wb')
        testlist = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
        print("用例总数：", testlist.countTestCases())
        runner = TestRunner(testlist, filename=report_name, report_dir=report_path, title="报告名", tester="张宇PM",desc="余董执行的测试报告", templates=2)
        runner.rerun_run(count=0, interval=2)
        # 调用getSuite函数返回值
        #runner.run(getSuite)
        fp.close()

    def get_report_file(self):
        report_path = os.path.join((os.path.dirname(__file__)), 'report')  # 用例文件夹
        '''第三步：获取最新的测试报告'''
        lists = os.listdir(report_path)
        lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
        print(u'最新测试生成的报告： ' + lists[-1])
        # 找到最新生成的报告文件
        report_file = os.path.join(report_path, lists[-1])
        return report_file

    def main_run(self):
        self.makelog("================================== 测试开始 ==================================")
        '''批量执行测试用例'''
        unittest.TextTestRunner(verbosity=2).run(self.getSuite())
        self.run_case(self.getSuite())  # 2执行用例
        self.get_report_file()
        self.makelog("================================== 测试结束 ==================================")


if __name__ == '__main__':
    Runner().main_run()
