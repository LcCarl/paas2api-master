# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 9:56
# @Author  : Jeico
# @File    : app_init.py
import pandas as pd
from tools.project_path import *
from data_init.common_data import CommonData


class CameraInit:

    # 测试版本
    Version = CommonData.Version
    # 登录账号
    LoginCode = CommonData.app_code
    # 登录密码
    LoginPwd = CommonData.app_pwd
