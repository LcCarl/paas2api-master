# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 16:25
# @Author  : Jeico
# @File    : system_management_init.py

from data_init.common_data import CommonData
from tools.base_def import BaseDef

# 时间戳
my_timestamp = BaseDef().time_stamp()
rand = BaseDef().random_number()


class AlarmInit:
    # 测试版本
    version = CommonData.Version
    # 通用默认每页显示条数
    PageSize = 10
    '''---------------------------------------告警相关接口--------------------------------------------------'''
    # 告警类型
    alarmType = 'TOWER_TEMP_LOW'
    # 页码
    pageNo = 1
    # 项目id  信友空冷
    projectId = 689
    # 机组id  1#机组
    unitLd = 519
    # 查询开始时间
    # beginTime='2021-03-01 14:19:30'
    beginTime = "2021-03-01 14:19:30"
    # 查询结束时间
    endTime = "2021-03-05 14:19:30"
    # 编辑告警规则  循环水冷水母管温度

    triggerValue = float(rand(1, 16))

    # 存储数据库返回值
    query_id = None
    '''--------------------------------------------项目概览相关接口---------------------------------------------------'''
    # 项目编码
    projectCode = 28
    # 机组编码
    unitCode = 521

    # 扇区编码
    sectionNo = 2
