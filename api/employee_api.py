#导包
import requests
from app import BASE_URL,headers_data
from utils import get_json
#创建一个类
class EmployeeApi:

    def __init__(self):
        self.add_emp_url = BASE_URL + "/api/sys/user"
        self.emp_url = BASE_URL + "/api/sys/user/{}"


    #添加员工的方法
    def add_emp(self,username,mobile,workNumber):
        add_emp_data = {"username": username,
                        "mobile": mobile,
                        "timeOfEntry": "2019-07-01",
                        "formOfEmployment": 1,
                        "workNumber": workNumber,
                        "departmentId": "1066240656856453120",
                        "correctionTime": "2019-11-30"}
        response = requests.post(self.add_emp_url,json=add_emp_data,headers=headers_data)
        return get_json(response)

    #查询员工
    def search_emp(self,emp_id):
        self.search_emp_url = self.emp_url.format(emp_id)
        response = requests.get(self.search_emp_url,headers=headers_data)
        return get_json(response)

    #修改员工
    def update_emp(self,username,emp_id):
        self.update_emp_url = self.emp_url.format(emp_id)
        update_emp_data = {"username":username}
        response = requests.put(self.update_emp_url,json=update_emp_data,headers=headers_data)
        return get_json(response)

    #删除员工
    def delete_emp(self,emp_id):
        self.delete_emp_url = self.emp_url.format(emp_id)
        response = requests.delete(self.delete_emp_url,headers=headers_data)
        return get_json(response)