# -*- coding:utf-8 -*-
import logging,os,time
log_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Logs')
print(log_path)
if os.path.exists('Logs') and os.path.isdir('Logs'):
     pass
else:
    os.mkdir('Logs')
logger = logging.getLogger()
logger.handlers.clear()  # 清除logger,避免多个文件引用重复打印log
logger.setLevel(logging.INFO)
nowTime = time.strftime('%Y%y%d')
logname = os.path.join(log_path + '\Log' + nowTime + '.log')  # 指定输出的日志文件名
print(logname)

class GetLog():
    def makelog(self,log_content):
        log_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Logs')
        if os.path.exists('Logs') and os.path.isdir('Logs'):
            pass
        else:
            os.mkdir('Logs')
        logger = logging.getLogger()
        logger.handlers.clear()  # 清除logger,避免多个文件引用重复打印log
        logger.setLevel(logging.INFO)
        nowTime = time.strftime('%Y%y%d')
        logname = os.path.join(log_path + '\Log' + nowTime + '.log')  # 指定输出的日志文件名
        print(logname)
        fh = logging.FileHandler(logname,encoding='utf-8')  # 指定utf-8格式编码，避免输出的日志文本乱码
        fh.setLevel(logging.DEBUG)
        # 创建一个handler，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.info(log_content)
        fh.close()

