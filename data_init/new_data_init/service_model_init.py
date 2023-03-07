# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 2:02 下午
# @Author  : Jeico
# @File    : service_model_init.py
from data_init.common_data import CommonData
from tools.base_def import BaseDef

my_timestamp = BaseDef().time_stamp()


class ServiceModelInit:
    # 通用默认每页显示条数
    PageSize = CommonData.PageSize
    # 修改每页显示条数
    ChangeSize = CommonData.ChangeSize

    # 物模型
    ThingModelCode = my_timestamp()
    ThingModelCode_cur = None
    ThingModelCode2 = my_timestamp()
    ThingModelCode2_cur = None
    ThingModelId = None

    # 物模型属性
    ModelCustomCode1 = my_timestamp()
    ModelCustomCode1_cur = None
    ModelCustomCode2 = my_timestamp()
    ModelCustomCode2_cur = None
    ModelCustomId = None

    # 物模型点位
    ThingModelItemCode1 = my_timestamp()
    ThingModelItemCode1_cur = None
    ThingModelItemCode2 = my_timestamp()
    ThingModelItemCode2_cur = None
    ThingModelItemCode3 = my_timestamp()
    ThingModelItemCode3_cur = None
    ThingModelItemCode4 = my_timestamp()
    ThingModelItemCode4_cur = None
    ThingModelItemCode5 = my_timestamp()
    ThingModelItemCode5_cur = None
    ThingModelItemId = None

    # 物模型实例
    ThingModelInstanceCode = my_timestamp()
    ThingModelInstanceCode_cur = None
    ThingModelInstanceId = None
    ThingModelInstanceItemId = None

    # 物模型实例属性
    ModelInstanceCustomCode1 = my_timestamp()
    ModelInstanceCustomCode1_cur = None
    ModelInstanceCustomCode2 = my_timestamp()
    ModelInstanceCustomCode2_cur = None
    ModelInstanceCustomId = None

    # 报警
    AlarmName = my_timestamp()
    AlarmName_cur = None
    AlarmId = None
