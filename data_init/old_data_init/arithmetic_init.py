# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 17:07
# @Author  : Jeico
# @File    : arithmetic_init.py
from data_init.common_data import CommonData
from tools.base_def import BaseDef

my_timestamp=BaseDef().time_stamp()
class ArithmeticInit:

    # 测试版本
    Version=CommonData.Version
    # 通用默认每页显示条数
    PageSize=CommonData.PageSize
    # 修改每页显示条数
    ChangeSize=CommonData.ChangeSize

    # 算法ID
    ArithmeticItemId=CommonData.ArithmeticItemId_created
    # 摄像头表ID
    CameraId=CommonData.CameraId_created