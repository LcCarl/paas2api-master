# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 19:50
# @Author  : Jeico
# @File    : project_path.py
import os

'''专门读取路径的值'''
# 顶级目录
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 测试报告的目录
test_report_bag = os.path.join(project_path, "results", "reports")
# 日志文件的目录
test_logs_path = os.path.join(project_path, "results", "logs")
# 运行配置目录
run_path = os.path.join(project_path, "conf", "run.config")

# 配置测试用例的目录
config_path = os.path.join(project_path, "conf", "case.config")
new_config_path = os.path.join(project_path, "conf", "case_new.config")

'''--------------------新平台——测试用例的目录-------------------------'''
# 新平台
new_test_case = os.path.join(project_path, "data_excel", "new_data_excel")
# 旧平台
old_test_case = os.path.join(project_path, "data_excel", "old_data_excel")
# 空冷平台
air_cooling = os.path.join(project_path, "data_excel", "aircooling_data_excel")
