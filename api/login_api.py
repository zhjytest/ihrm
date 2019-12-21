#导包
import requests
from app import BASE_URL
from utils import get_json


#创建一个类
class LoginApi:


    def __init__(self):
        self.login_url = BASE_URL + "/api/sys/login"



    #登录接口
    def login(self,mobile,password):
        login_data = {}
        response = None
        if mobile:
            login_data['mobile'] = mobile
        if password:
            login_data['password'] = password
        if login_data:
            response = requests.post(self.login_url,json=login_data)
        else:
            response = requests.post(self.login_url)
        return get_json(response)
        # status_code = response.status_code
        # result = response.json()
        # result['status_code'] = status_code
        # return result



if __name__ == '__main__':
    lg = LoginApi()
    lg_result = lg.login(None,None)
    print(lg_result)



