# -*- coding: utf-8 -*-
# coding: utf-8
# @Time    : 2020/8/19 21:02
# @Author  : Jeico
# @File    : analysis_management_init.py

import pandas as pd
from tools.project_path import *
from data_init.common_data import CommonData
from tools.base_def import BaseDef

my_timestamp = BaseDef().time_stamp()
test_case_analysis = os.path.join(old_test_case, "test_case_analysis.xlsx")


class AnalysisManagementInit:
    # 测试版本
    Version1 = CommonData.Version

    '''————趋势组管理——————'''

    # 通用默认每页显示条数
    PageSize = CommonData.PageSize
    # 修改每页显示条数
    ChangeSize = CommonData.ChangeSize

    # 趋势组的开始时间、结束时间
    StaTime = CommonData.StaTime
    MidTime = CommonData.MidTime
    EndTime = CommonData.EndTime

    # 创建新的趋势组
    GroupName = my_timestamp()
    # 创建完之后的趋势组名，用于当前的sql和期望值替换
    GroupName_cur = None
    # 获取最新创建的趋势组id
    GroupId = None

    # 趋势组频率
    Frequency = pd.read_excel(test_case_analysis, sheet_name="init").iloc[3, 2]
    # 聚合公式
    Formula = pd.read_excel(test_case_analysis, sheet_name="init").iloc[4, 2]
    # 测点id和测点位置
    DeviceItemId = pd.read_excel(test_case_analysis, sheet_name="init").iloc[5, 2]
    Location = pd.read_excel(test_case_analysis, sheet_name="init").iloc[6, 2]

    # 设备ID
    DeviceID = CommonData.DeviceID_created
    # 设备类型CODE
    DevTypeCode = CommonData.DevTypeCode_created
    # 设备点位表ID
    DevItemId = CommonData.DevItemId_created
    # 物联点位code
    ItemCode = CommonData.ItemCode_created


if __name__ == '__main__':
    a = AnalysisManagementInit().GroupName
    print(type(a))
