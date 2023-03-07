# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 2:20 下午
# @Author  : Jeico
# @File    : service_agent_init.py

from data_init.common_data import CommonData
from tools.base_def import BaseDef

my_timestamp = BaseDef().time_stamp()


class ServiceAgentInit:

    PageSize = CommonData.PageSize
    ChangeSize = CommonData.ChangeSize
    # 登陆账号
    LoginCode = CommonData.login_code
    LoginPwd = CommonData.login_pwd

    # 创建新网关编号
    CameraAgentCode = CommonData.CameraAgentCode
    AgentCode = my_timestamp()
    AgentCode_cur = None
    AgentId = None
    # 协议
    Protocol = "JeicoLink"
    Protocol2 = "ZouLink"

    # 创建新测点
    AgentItemNum = my_timestamp()
    AgentItemNum_cur = None
    AgentItemNum2 = my_timestamp()
    AgentItemNum2_cur = None
    AgentItemNum3 = my_timestamp()
    AgentItemNum3_cur = None

    # 属性
    MetaDataCode = my_timestamp()
    MetaDataCode_cur = None

    # 物模型变量
    ThingModelCode = my_timestamp()
    ThingModelCode_cur = None
    # 物模型点位
    ThingModelItemCode1 = my_timestamp()
    ThingModelItemCode1_cur = None
    ThingModelItemCode2 = my_timestamp()
    ThingModelItemCode2_cur = None
    ThingModelItemCode3 = my_timestamp()
    ThingModelItemCode3_cur = None
    # 物模型实例
    ThingModelInstanceCode = my_timestamp()
    ThingModelInstanceCode_cur = None


