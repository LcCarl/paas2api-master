# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 15:04
# @Author  : Jeico
# @File    : http_request.py

import requests
import time
from tools.my_log import MyLog
from conf.environment_config import EnvironmentConfig

my_logger = MyLog()


class HttpRequest:

    @staticmethod
    def http_request_common(method, test_api, api_data=None, token=None):
        """————————通用requests请求封装——————————
        参数：
            method:请求方式 支持get 以及post ，str ；
            test_api:请求的接口port，str ；
            api_data:传递的参数 非必填参数 ，dic ；
            token:请求的时候传递的token值，str；
        返回： 接口响应结果的消息实体 ；
        ——————————————————————————————————————"""
        api_url = EnvironmentConfig().CommonUrl + test_api

        if EnvironmentConfig().environment_type == 5:
            if token:
                api_headers = {'Content-Type': 'application/json;charset=UTF-8',
                               "Authorization": "bearer " + token}
            else:
                api_headers = {'Content-Type': 'application/json;charset=UTF-8',
                               "Authorization": "bearer "}
        else:
            api_headers = {'Content-Type': 'application/json;charset=UTF-8',
                           "token": token}

        # s = requests.session()
        # s.keep_alive = False

        try:
            if (method.lower() in ['get', 'patch']) and type(api_data) is dict:
                res = requests.request(method, api_url, params=api_data, headers=api_headers)
            else:
                res = requests.request(method, api_url, json=api_data, headers=api_headers)
        except Exception as e:
            my_logger.error("请求报错了：{}".format(str(e)))
            raise e
        time.sleep(5)
        return res

    @staticmethod
    def http_request_login(method, test_api, api_data):
        """当环境类型为5时，登陆，专用请求"""
        api_url = EnvironmentConfig().CommonUrl + test_api
        try:
            res = requests.request(method, api_url, data=api_data)
        except Exception as e:
            my_logger.error("请求报错了：{}".format(str(e)))
            raise e
        return res


if __name__ == '__main__':
    data1 = {"username": "APItest",
             "password": "Hundunyun@123",
             "grant_type": "password",
             "client_id": "paasweb",
             "client_secret": "paasweb"}
    res1 = HttpRequest().http_request_login("post", "ac/oauth/token", data1)
    token = res1.json()["data"]["access_token"]
    print(token)
    data2 = {}
    res2 = HttpRequest().http_request_common("POST", "service-paas-script/mgnt/script/addScript", data2, token)
    print(res2.json())
