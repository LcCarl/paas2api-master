# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 5:30 下午
# @Author  : Jeico
# @File    : service_user_init.py

from data_init.common_data import CommonData
from tools.base_def import BaseDef

my_timestamp = BaseDef().time_stamp()


class ServiceUserInit:
    # 注册用户
    Account = my_timestamp()
    Email = BaseDef().get_email()
    Phone = BaseDef().get_phone()
    Account_cur = None
    Email_cur = None
    Phone_cur = None
    # 返回的t_user表ID
    UserID = None
    # 小程序的appId
    AppID = CommonData.app_id

