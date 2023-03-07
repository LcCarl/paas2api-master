# -*- coding: utf-8 -*-
# coding: utf-8
# @Time    : 2020/8/19 21:02
# @Author  : Jeico
# @File    : cim_management_init.py

import pandas as pd
from tools.project_path import *
from data_init.common_data import CommonData
from tools.base_def import BaseDef

my_timestamp=BaseDef().time_stamp()

class CimManagementInit:

    # 测试版本
    Version = "v1"


    '''---------------平台标准管理------------------'''

    #通用默认每页显示条数
    PageSize = CommonData.PageSize
    #修改每页显示条数
    ChangeSize = CommonData.ChangeSize

    '''------------------------平台标准管理接口-------------------------'''
    # 创建完之后的平台标准code，用于当前的sql和期望值的替换
    CimTypeName = my_timestamp()
    CimTypeCode_cur = None
    # 获取最新创建的平台标准id
    CimTypeId = my_timestamp

    '''-----------------------平台标准目录管理接口---------------------------'''
    # 创建新的平台标准目录
    NodeName = my_timestamp()
    NodeName_cur = None
    # 获取标准目录的id
    CimNodeId = None

    '''-------------------平台标准属性管理接口---------------------'''
    # 此ID仅从sql中获取
    CimPropertyId = None
    CimPropertyName = my_timestamp()
    CimPropertyCode = None
    CimPropertyName_cur = None
    CimPropertyCode_cur = None
    # 获取在测试基本属性和物联点位中使用到属性信息的code
    CimPropertyCodeInParam = None

    '''---------------------基本属性管理接口------------------------'''
    # 随机产生属性信息的名称，别名
    CimPropertyParamName = my_timestamp()
    CimPropertyParamAlias = my_timestamp()
    CimPropertyParamAlias_cur = None
    CimPropertyParamName_cur = None
    CimPropertyParamId = None
    # 由sql查询
    CimparamIds = None

    '''-----------------平台标准物联点位管理接口-----------------------'''
    CimPropertyItemAlias_cur = None
    CimPropertyItemName_cur = None
    CimPropertyItemItemId_cur = None
    # 获取最新创建的物联点位的id
    CimPropertyItemId = None
    # 获取最新创建的自定义点位id
    CustomItemId = None

    '''--------------------主题目录管理接口---------------------------'''
    # 创建项目
    ProjectName = my_timestamp()
    ProjectId = None
    # 创建新的主题目录名称
    SubjectCatalogName = my_timestamp()
    # 创建完之后的主题目录的名称，用于当前的sql和期望值替换
    SubjectCatalogName_cur = None
    # 获取最新创建的主题目录id
    SubjectCatalogId = None
    # 获取最新创建的主题目录的code
    SubjectCatalogCode = None
    # 获取最新创建的主题目录的物联点位的id
    SubjectCatalogItemId = None



if __name__ == '__main__':
    a=CimManagementInit().GroupName
    print(type(a))