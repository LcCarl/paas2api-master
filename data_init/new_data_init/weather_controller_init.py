# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 10:30 上午
# @Author  : Jeico
# @File    : weather_controller_init.py

from data_init.common_data import CommonData


class WeatherControllerInit:
    # 测试版本
    Version = CommonData.Version

    # 查询区域
    AdCode = "110101"
    AdIP = "124.64.101.65"
    Longitude = "116.416357"
    Latitude = "39.928353"
    Province = "北京市"
    City = "北京市"
    District = "东城区"

    # 预测时间
    NowTime = "2021-06-11 00:00:00"
    PastTime = "2021-06-07 00:00:00"
    FutureTime = "2021-06-17 00:00:00"


