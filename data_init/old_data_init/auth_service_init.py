# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 14:14
# @Author  : Jeico
# @File    : auth_service_init.py


import pandas as pd
from tools.project_path import *
from data_init.common_data import CommonData

test_case_user = os.path.join(old_test_case, "test_case_user.xlsx")


class AuthServiceInit:
    # 测试版本
    Version = CommonData.Version
    # 用户
    TenantCode = CommonData.login_code
    TenantPwd = CommonData.login_pwd

    '''————用户——————'''

    # 注册账号
    UserCode = pd.read_excel(test_case_user, sheet_name="init").iloc[0, 2]
    # 注册完的当前账号，用于当前的sql和期望值替换
    UserCode_cur = None
    # 获取最新创建的网关ID
    UserId = None


