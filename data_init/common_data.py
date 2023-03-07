# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 16:52
# @Author  : Jeico
# @File    : common_data.py

"""——————此页为所有模块的通用数据——————————————————"""


class CommonData:
    """——全局参数——"""
    # 设置token初始值
    token = None
    # 测试版本
    Version = "v1"
    # 接口测试耗费时间列表
    TimeList = []
    TimeConsuming = {}

    # 登录账号
    login_code = "APItest"
    login_pwd = "Hundunyun@123"
    tenant_id = "28"

    # 小程序的appId
    app_id = "wx6a7f14a26e237c95"

    '''——页面查询——'''
    # 默认每页的条数
    PageSize = 20
    # 修改每页的条数
    ChangeSize = 1

    # 可用的摄像头编号
    CameraAgentCode = "E49801303"

    # ——————————————下面是中台1.0————————————————
    # app测试账号
    app_code = "APP_WY_WK_001"
    app_pwd = "hdy@0508"

    '''——时间查询——'''
    StaTime = "20201125000000"
    MidTime = "20201125155959"
    EndTime = "20201125235959"

    '''——创建参数——'''
    # 项目ID
    ProjectID_created = 188
    # 组态ID
    ConfigurationId_created = 129
    # 设备ID
    DeviceID_created = "FC_0120201125161429060549"
    # 设备类型CODE
    DevTypeCode_created = "FCT_0120201125161103539529"
    # 设备点位表ID
    DevItemId_created = 1848
    # 物联点位code
    ItemCode_created = "WLDW_0120201125161157568017"
    # 算法输出点位ID
    ArithmeticItemId_created = "SFDW_0120201209170442733394"
    # 摄像头表ID
    CameraId_created = 119
    # 主题目录表ID
    SubjectId_created = 271

