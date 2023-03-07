# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 4:18 下午
# @Author  : Jeico
# @File    : auth_service_init.py
from data_init.common_data import CommonData
from tools.base_def import BaseDef

my_timestamp = BaseDef().time_stamp()


class AuthServiceInit:

    PageSize = CommonData.PageSize
    ChangeSize = CommonData.ChangeSize

    # 登陆账号
    LoginCode = CommonData.login_code
    LoginPwd = CommonData.login_pwd
    # 域
    RentName = my_timestamp()
    RentName_cur = None
    RentID = None
    # 角色
    RoleName = my_timestamp()
    RoleName_cur = None
    RoleID = None
    # 用户
    Account = my_timestamp()
    Email = BaseDef().get_email()
    Phone = BaseDef().get_phone()
    Account_cur = None
    Email_cur = None
    Phone_cur = None
    UserID = None
    DataUserID = None

    # 项目
    ProjectName = my_timestamp()
    ProjectName_cur = None
    ProjectID = None
    ProjectNo = None

