# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 16:25
# @Author  : Jeico
# @File    : system_management_init.py

from data_init.common_data import CommonData
from tools.base_def import BaseDef

my_timestamp = BaseDef().time_stamp()


class SystemManagementInit:
    # 测试版本
    Version = CommonData.Version
    # 通用默认每页显示条数
    PageSize = CommonData.PageSize
    # 修改每页显示条数
    ChangeSize = CommonData.ChangeSize
    # 用户
    TenantCode = CommonData.login_code
    TenantPwd = CommonData.login_pwd
    TenantId = CommonData.tenant_id

    '''————系统管理——————'''
    # 创建新的系统字典名
    DictionaryName = my_timestamp()
    # 创建完之后的系统字典名，用于当前的sql和期望值替换
    DictionaryName_cur = None
    # id获取创建的系统字典的no
    DictionaryName_nos = []
    # 获取创建的字典ID
    DictionaryName_ids = []

    '''————项目管理——————'''
    # 创建新项目名称
    ProjectName = my_timestamp()
    # 创建完之后的项目名称，用于当前的sql和期望值替换
    ProjectName_cur = None
    # 获取最新创建的项目的No
    ProjectNo = None
    # 获取最新创建的项目的ID
    ProjectID = None

    '''————标签管理——————'''
    # 创建新标签
    TagName = my_timestamp()
    # 创建完之后的标签，用于当前的sql和期望值替换
    TagName_cur = None
    # 获取最新创建的标签的ID
    TagID = None
    # 获取最新创建的标签的code
    TagCode = None
