#导包
import unittest
from api.employee_api import EmployeeApi
from utils import common_assert,mysql
import logging
import pymysql
from parameterized import parameterized
from app import BASE_DIR
import json

#读取添加员工的数据
#[(),()]
def add_build_data():
    test_data = []
    with open(BASE_DIR+"/data/employee.json",encoding='UTF-8') as f:
        datas = json.load(f)
        add_emp_data = datas.get('add_emp_data')
        username = add_emp_data.get('username')
        mobile = add_emp_data.get('mobile')
        workNumber = add_emp_data.get('workNumber')
        status_code = add_emp_data.get('status_code')
        success = add_emp_data.get('success')
        code = add_emp_data.get('code')
        message = add_emp_data.get('message')
        test_data.append((username,mobile,workNumber,status_code,success,code,message))
    return test_data


#读取查询员工的数据
def search_build_data():
    test_data = []
    with open(BASE_DIR+"/data/employee.json",encoding='UTF-8') as f:
        datas = json.load(f)
        search_emp_data = datas.get('search_emp_data')
        status_code = search_emp_data.get('status_code')
        success = search_emp_data.get('success')
        code = search_emp_data.get('code')
        message = search_emp_data.get('message')
        test_data.append((status_code,success,code,message))
    return test_data


#读取修改员工的数据
def update_build_data():
    test_data = []
    with open(BASE_DIR+"/data/employee.json",encoding='UTF-8') as f:
        datas = json.load(f)
        update_emp_data = datas.get('update_emp_data')
        username = update_emp_data.get('username')
        status_code = update_emp_data.get('status_code')
        success = update_emp_data.get('success')
        code = update_emp_data.get('code')
        message = update_emp_data.get('message')
        test_data.append((username,status_code,success,code,message))
    return test_data


#获取删除员工的数据
def delete_build_data():
    test_data = []
    with open(BASE_DIR+"/data/employee.json",encoding='UTF-8') as f:
        datas = json.load(f)
        delete_emp_data = datas.get('delete_emp_data')
        status_code = delete_emp_data.get('status_code')
        success = delete_emp_data.get('success')
        code = delete_emp_data.get('code')
        message = delete_emp_data.get('message')
        test_data.append((status_code,success,code,message))
    return test_data

#新建测试类
class TestEmployee(unittest.TestCase):

    employee_id = "1207602501284876288"

    @classmethod
    def setUpClass(cls):
        cls.emp = EmployeeApi()

    #添加员工
    @parameterized.expand(add_build_data)
    def test01_add_emp(self,username,mobile,workNumber,status_code,success,code,message):
        #初始化数据
        # username = "tom02"
        # mobile = "13612001001"
        # workNumber = "1001"
        #请求被测接口
        result = self.emp.add_emp(username,mobile,workNumber)
        logging.info("add emp data:{}".format(result))
        #断言
        common_assert(self,result,status_code,success,code,message)

        #获取员工id
        TestEmployee.employee_id = result.get('data').get('id')

    # def test01_add_emp_01(self):
    #     #初始化数据
    #     username = None
    #     mobile = None
    #     workNumber = None
    #     #请求被测接口
    #     result = self.emp.add_emp(username,mobile,workNumber)
    #     logging.info("add emp data:{}".format(result))
    #     #断言
    #     #common_assert(self,result,status_code,success,code,message)


    #查询员工
    @parameterized.expand(search_build_data)
    def test02_search_emp(self,status_code,success,code,message):
        #初始化数据

        #请求被测接口
        result = self.emp.search_emp(TestEmployee.employee_id)
        logging.info("serach emp data:{}".format(result))
        #断言
        common_assert(self,result,status_code,success,code,message)

    #修改员工
    @parameterized.expand(update_build_data)
    def test03_update_emp(self,username,status_code,success,code,message):
        #初始化数据
        #username = "tome_old"
        #请求被测接口
        result = self.emp.update_emp(username,TestEmployee.employee_id)
        logging.info("update emp data:{}".format(result))
        #断言
        common_assert(self,result)
        #self.assertEqual(TestEmployee.employee_id,result.get('data').get('id'))
        #================================
        #创建数据库对象
        # conn = pymysql.connect("182.92.81.159", "readuser", "iHRM_user_2019", "ihrm")
        # #创建游标对象
        # cursor = conn.cursor()
        # #执行操作
        # sql = "select username from bs_user where id = %s"
        # cursor.execute(sql,TestEmployee.employee_id)
        # one_data = cursor.fetchone()
        # logging.info("one_data:{}".format(one_data))
        # update_username = one_data[0]
        # self.assertEqual(username,update_username)
        # #关闭游标
        # cursor.close()
        # #关闭连接对象
        # conn.close()

        #使用封装后的mysql类
        sql = "select username from bs_user where id = %s"
        one_data = mysql().get_one(sql,TestEmployee.employee_id)
        update_username = one_data[0]
        self.assertEqual(username,update_username)

    #删除员工
    @parameterized.expand(delete_build_data)
    def test04_delete_emp(self,status_code,success,code,message):
        #初始化数据
        #请求被测接口
        result = self.emp.delete_emp(TestEmployee.employee_id)
        logging.info("delete emp data:{}".format(result))
        #断言
        common_assert(self,result)