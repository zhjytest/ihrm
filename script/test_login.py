#导包
import unittest
from api.login_api import LoginApi
from utils import common_assert
import logging
from app import TOKEN,headers_data,BASE_DIR
from parameterized import parameterized
import json

#读取登录数据
#[(),(),()]
def build_data():
    test_data = []
    with open(BASE_DIR+'/data/login.json',encoding='UTF-8') as f:
        datas = json.load(f)
        for dt in datas:
            mobile = dt.get('mobile')
            password = dt.get('password')
            status_code = dt.get('status_code')
            success = dt.get('success')
            code = dt.get('code')
            message = dt.get('message')
            test_data.append((mobile,password,status_code,success,code,message))
    return test_data


#建测试类
class TestLogin(unittest.TestCase):

    #初始化
    @classmethod
    def setUpClass(cls):
        cls.lg_api = LoginApi()


    #登录成功
    @parameterized.expand(build_data)
    def test_login(self,mobile,password,status_code,success,code,message):
        #调用被测接口
        result = self.lg_api.login(mobile,password)
        logging.info("login success data:{}".format(result))
        #断言
        common_assert(self,result,status_code,success,code,message)
        #common_assert(self,result,200,True,10000,'操作成功')
        # self.assertEqual(200,result.get('status_code'))
        # self.assertEqual(True,result.get('success'))
        # self.assertEqual(10000,result.get('code'))
        # self.assertIn('操作成功',result.get('message'))

        #提取token
        str_data = result.get('data')
        if str_data:
            TOKEN = 'Bearer '+ str_data
            print(TOKEN)
            headers_data['Authorization'] = TOKEN


    #登录成功
    #@unittest.skip
    def test_login_success(self):
        #初始化数据
        mobile = "13800000002"
        password = "123456"
        #调用被测接口
        result = self.lg_api.login(mobile,password)
        logging.info("login success data:{}".format(result))
        #断言
        common_assert(self,result)
        #common_assert(self,result,200,True,10000,'操作成功')
        # self.assertEqual(200,result.get('status_code'))
        # self.assertEqual(True,result.get('success'))
        # self.assertEqual(10000,result.get('code'))
        # self.assertIn('操作成功',result.get('message'))

        #提取token
        str_data = result.get('data')
        if str_data:
            TOKEN = 'Bearer '+ str_data
            print(TOKEN)
            headers_data['Authorization'] = TOKEN

    #用户名不存在
    @unittest.skip
    def test_username_is_not_exist(self):
        #初始化数据
        mobile = "12888889999"
        password = "123456"
        #调用被测接口
        result = self.lg_api.login(mobile,password)
        #断言
        common_assert(self,result,200,False,20001,'用户名或密码错误')
        # self.assertEqual(200,result.get('status_code'))
        # self.assertEqual(False,result.get('success'))
        # self.assertEqual(20001,result.get('code'))
        # self.assertIn('用户名或密码错误',result.get('message'))

    #密码错误
    @unittest.skip
    def test_password_is_error(self):
        #初始化数据
        mobile = "13800000002"
        password = "error"
        #请求被测接口
        result = self.lg_api.login(mobile,password)
        #断言
        common_assert(self,result,200,False,20001,'用户名或密码错误')
        # self.assertEqual(200,result.get('status_code'))
        # self.assertEqual(False,result.get('success'))
        # self.assertEqual(20001,result.get('code'))
        # self.assertIn('用户名或密码错误',result.get('message'))

    #请求参数为空
    @unittest.skip
    def test_parms_is_null(self):
        #初始化数据
        mobile=None
        password = None
        #请求被测接口
        result = self.lg_api.login(mobile,password)
        #断言
        common_assert(self,result,200,False,99999,'系统繁忙')


    #用户名为空
    @unittest.skip
    def test_username_is_null(self):
        #初始化数据
        mobile = ""
        password = "123456"
        #请求被测接口
        result = self.lg_api.login(mobile,password)
        #断言
        common_assert(self,result,200,False,20001,'用户名或密码错误')

    #密码为空
    @unittest.skip
    def test_password_is_null(self):
        #初始化数据
        mobile = "13800000002"
        password = ""
        #请求被测接口
        result = self.lg_api.login(mobile,password)
        #断言
        common_assert(self,result,200,False,20001,'用户名或密码错误')