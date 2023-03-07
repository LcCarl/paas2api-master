# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 16:38
# @Author  : Jeico
# @File    : alarm_init.py
from data_init.common_data import CommonData
from tools.base_def import BaseDef

my_timestamp = BaseDef().time_stamp()


class AlarmInit:
    # 测试版本
    Version = CommonData.Version
    # 通用默认每页显示条数
    PageSize = CommonData.PageSize
    # 修改每页显示条数
    ChangeSize = CommonData.ChangeSize
