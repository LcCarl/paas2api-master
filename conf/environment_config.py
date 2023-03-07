# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 11:50
# @Author  : Jeico
# @File    : environment_config.py

from tools.project_path import *
from tools.do_config import DoConfig

"""——————此页为环境配置，用于编辑切换的运行环境内容——————————————————"""


class EnvironmentConfig:
    # 从配置文件读取environment_type的值
    environment_type = eval(DoConfig().read_config(run_path, "platform", "run_list"))

    if environment_type == 5:
        """————————新的paas，测试环境——————"""
        # api地址
        CommonUrl = "http://test.venus.wxhundun.com/"
        # 数据库
        db_config = {"host": "10.88.33.208",
                     "user": "root",
                     "password": "#20as3SElksds0ew98!",
                     "port": 3306}
        # 测试用例配置
        test_config_path = new_config_path  # new_config_path  ， config_path
        test_case_bag = new_test_case
        test_init = "data_init.new_data_init."
        test_report_path = test_report_bag + "/report_PaasNew.html"

        # 数据库和模块的对应关系， 一个init文件对应一个模块
        init_database = {
            "auth_service_init": "auth_service",  # 2.0第一个版本
            "service_user_init": "service-user",
            "service_agent_init": "service-agent",
            "service_model_init": "service-model"
        }




