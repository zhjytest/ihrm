#导包
import unittest
from script.test_login import TestLogin
from script.test_employee import TestEmployee
from tools.HTMLTestRunner import HTMLTestRunner
from app import BASE_DIR
import time


#组装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))




#生成测试报告
file_path = BASE_DIR+"/report/report_{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
with open(file_path,'wb') as f:
    runner = HTMLTestRunner(f,title='ihrm测试报告',description='v1.0')
    runner.run(suite)
