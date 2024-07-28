#!/use/bin/env python
# coding:utf-8
import unittest,smtplib,time,os
from unittestreport import TestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.log import GetLog


class Runner(GetLog):
    def getSuite(self):
        '''获取要执行的测试套件'''
        suite = unittest.TestLoader().discover(
            start_dir=os.path.join((os.path.dirname(__file__)), 'testcases'),
            pattern='test_*.py',
            top_level_dir=None)
        return suite

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
        report_path = os.path.join((os.path.dirname(__file__)), 'report')  # 报告文件夹
        '''第三步：获取最新的测试报告'''
        lists = os.listdir(report_path)
        lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
        print(u'最新测试生成的报告：' + lists[-1])
        # 找到最新生成的报告文件
        report_file = os.path.join(report_path, lists[-1])
        return report_file

    def get_log_file(self):
        log_path = os.path.join((os.path.dirname(__file__)),'logs')
        logs = os.listdir(log_path)
        logs.sort(key=lambda fn: os.path.getmtime(os.path.join(log_path,fn)))



    def get_image_file(self):
        image_path = os.path.join((os.path.dirname(__file__)),'logs')
        image = os.listdir(image_path)
        image.sort()

    def send_mail(self):
        filepath = Runner().get_report_file()   #获取最新报告地址
        smtpsever = 'smtp.qq.com'
        sender = '1910572937@qq.com'
        psw = 'iouzyaxjjjvkbhhi'
        receiver = '1910572937@qq.com'
        port = 465
        filepath = filepath
        with open(filepath, 'rb') as fp:
            mail_body = fp.read()
        msg = MIMEMultipart()
        msg['from'] = sender
        msg['to'] = receiver
        msg['subject'] = '带附件的邮件发送模板主题'

        body = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(body)
        att = MIMEText(mail_body, 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;fillename="test_report.html"'
        msg.attach(att)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpsever)
            smtp.login(sender, psw)
        except:
            smtp = smtplib.SMTP_SSL(smtpsever, port)
            smtp.login(sender, psw)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.send_message(msg,from_addr='1910572937@qq.com',to_addrs='1910572937@qq.com')
        smtp.quit()

    def main_run(self):
        self.makelog("================================== 测试开始 ==================================")
        '''批量执行测试用例'''
        unittest.TextTestRunner(verbosity=2).run(self.getSuite())
        self.run_case(self.getSuite())  # 2执行用例
        self.get_report_file()
        self.get_log_file()
        self.get_image_file()
        self.send_mail()
        self.makelog("================================== 测试结束 ==================================")


if __name__ == '__main__':
    Runner().main_run()