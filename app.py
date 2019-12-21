import logging
import logging.handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_URL = "http://182.92.81.159"

TOKEN = "Bearer c96fa665-1952-4aa8-b55c-0c406af99e5d"

headers_data = {"Content-Type": "application/json", "Authorization":TOKEN}

def log_init_conifg():

    #创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    #创建控制台输出器
    sh = logging.StreamHandler()
    #创建文件输出器
    log_file = BASE_DIR + "/log/ihrm.log"
    th = logging.handlers.TimedRotatingFileHandler(log_file,when="midnight",interval=1,backupCount=7,encoding='UTF-8')
    #创建格式化器
    fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formater = logging.Formatter(fmt)
    #把格式化器加入到输出器
    sh.setFormatter(formater)
    th.setFormatter(formater)
    #把格式化器加入到日志器
    logger.addHandler(sh)
    logger.addHandler(th)