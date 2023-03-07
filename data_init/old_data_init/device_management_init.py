# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 16:08
# @Author  : Jeico
# @File    : device_management_init.py

from data_init.common_data import CommonData
from tools.base_def import BaseDef

my_timestamp = BaseDef().time_stamp()
rand = BaseDef().random_number()


class DeviceManagementInit:
    # 测试版本
    Version = CommonData.Version
    # 通用默认每页显示条数
    PageSize = CommonData.PageSize
    # 修改每页显示条数
    ChangeSize = CommonData.ChangeSize

    Rand_0_2 = rand(0, 2)
    Rand_0_5 = rand(0, 5)

    # 设备编码
    DeviceID_created = CommonData.DeviceID_created
    # 设备类型编码
    DevTypeCode_created = CommonData.DevTypeCode_created
    # 项目ID
    ProjectID_created = CommonData.ProjectID_created
    # 组态ID
    ConfigurationId_created = CommonData.ConfigurationId_created

    '''————网关  和  测点——————'''

    # 创建新网关编号
    AgentNum = my_timestamp()
    # 创建完之后的网关编号，用于当前的sql和期望值替换
    AgentNum_cur = None
    # 获取最新创建的网关ID
    AgentId = None

    # 创建新测点编号
    AgentItemNum = my_timestamp()
    # 创建完之后的网关测点编号，用于当前的sql和期望值替换
    AgentItemNum_cur = None

    '''————设备：设备类型——————'''

    # 创建新的设备类型name
    DevTypeName = my_timestamp()
    # 创建完之后的设备类型name，用于当前的sql和期望值替换
    DevTypeName_cur = None
    # 设备类型code
    DevTypeCode = None
    # 获取最新创建的设备类型表ID
    DevTypeID = None

    '''————设备：物联点位——————'''
    # 物联点位名
    DevTypeItemName = my_timestamp()
    # 创建完之后的物联点位名，用于当前的sql和期望值替换
    DevTypeItemName_cur = None
    # 获取创建的物联点位编码
    DevTypeItemCode = None
    # 获取创建物联点位的表ID
    DevTypeItemID = None

    '''————设备：设备——————'''

    # 创建新的设备name
    DevName = my_timestamp()
    # 创建完之后的设备name，用于当前的sql和期望值替换
    DevName_cur = None
    # 设备code
    DevCode = None
    # 设备ID
    DevId = None

    '''————设备：标签——————'''
    # 创建新标签
    TagName = my_timestamp()
    # 创建完之后的标签，用于当前的sql和期望值替换
    TagName_cur = None
    # 获取最新创建的标签的ID
    TagID = None
    # 获取最新创建的标签的code
    TagCode = None


if __name__ == '__main__':
    print(DeviceManagementInit().DevTypeID)
