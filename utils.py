import pymysql

def get_json(response):
    status_code = response.status_code
    result = response.json()
    result['status_code'] = status_code
    return result


#公共的断言方法
def common_assert(test_case,result,status_code=200,success=True,code=10000,message='操作成功'):
    test_case.assertEqual(status_code,result.get('status_code'))
    test_case.assertEqual(success,result.get('success'))
    test_case.assertEqual(code,result.get('code'))
    test_case.assertIn(message,result.get('message'))


#连接mysql的类
class mysql(object):

    def __init__(self):
        self.conn =  pymysql.connect("182.92.81.159","readuser","iHRM_user_2019","ihrm")

    #def get_conn(self):


    #查询一条数据的方法
    def get_one(self,sql,parms=None):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql,parms)
                return cursor.fetchone()
        finally:
            self.conn.close()
