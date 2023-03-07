# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 14:09
# @Author  : Jeico
# @File    : test_http.py

import unittest
from ddt import ddt, data
from datetime import datetime
from tools.http_request import HttpRequest
from tools.my_log import MyLog
from tools.compare import Compare
from tools.base_def import BaseDef
from tools.processing_data import DataProcessing
from tools.regex_after_data import AfterDataRegex
from tools.do_response import DoResponse
from conf.environment_config import EnvironmentConfig
from tools.project_path import *
from data_init.common_data import CommonData
from tools.special_handling import SpecialHandling

my_logger = MyLog()
# 获取初始测试数据
test_data = DataProcessing.data_processing()


@ddt
class TestHttp(unittest.TestCase):

    def setUp(self):
        pass

    @data(*test_data)
    def test_http(self, get_data):
        # 处理测试数据
        init_path = BaseDef().get_import(get_data["init_path"])
        get_data = eval(AfterDataRegex().after_data_regex(str(get_data), get_data["init_path"]))
        test_case_path = os.path.join(EnvironmentConfig.test_case_bag, get_data["case_path"] + ".xlsx")
        my_logger.info("测试用例表格为：{}".format(test_case_path))

        if get_data["data"]:
            param = eval(get_data["data"])
            if get_data["precondition"]:
                response_data = DoResponse().do_response(get_data["precondition"], test_case_path)
                if get_data["key"]:
                    if get_data["key"].find(",") != -1:
                        key_new = get_data["key"].split(",")
                        for position, key in enumerate(key_new):
                            BaseDef().replace_data(param, key, response_data[position])
                    else:
                        BaseDef().replace_data(param, get_data["key"], response_data)
                else:
                    param.append(response_data)
        else:
            param = get_data["data"]

        if EnvironmentConfig().environment_type == 5 and ("service-agent/agent/delete/camera/" in get_data["api"]):
            SpecialHandling().camera_agent()

        my_logger.info("*****现在测试的内容是：{}模块，第{}行，{}*****".format(get_data["module"], get_data["id"], get_data["case_name"]))

        # ——————http请求测试——————
        my_logger.info("——————开始http请求：{}————————".format(EnvironmentConfig().CommonUrl+get_data["api"]))
        my_logger.info("——————http请求数据：{}————————".format(param))
        my_logger.info("——————http请求方式：{}————————".format(get_data["method"]))
        start = datetime.now()
        if EnvironmentConfig().environment_type == 5 and ("ac/oauth/token" in get_data["api"]):
            res = HttpRequest().http_request_login(
                get_data["method"], get_data["api"], param)
        else:
            res = HttpRequest().http_request_common(
                get_data["method"], get_data["api"], param, getattr(CommonData, "token"))
        end = datetime.now()

        # 将时间写进excel
        api_time = str((end - start).total_seconds())
        BaseDef.write_back(test_case_path, get_data["sheet"], get_data["id"] + 1, 11, api_time)

        my_logger.info("——————http耗时：{}————————".format(api_time))
        my_logger.info("——————完成http请求————————")
        my_logger.info("——————http请求结果：{}————————".format(res.text))

        # 处理接口耗时
        getattr(CommonData, "TimeList").append(eval(api_time))
        getattr(CommonData, "TimeConsuming")[
            get_data["api"]+"+"+get_data["sheet"]+"+"+str(get_data["id"])] = eval(api_time)

        # 获取response
        out_come = res.json()

        # 如果token有的话 那么就更新token
        if "token" in str(out_come["data"]):
            if "access_token" in str(out_come["data"]):
                setattr(CommonData, "token", out_come["data"]["access_token"])
            else:
                setattr(CommonData, "token", out_come["data"]["token"])

        # 断言  以及  写回code 、断言结果、response
        result = None
        try:
            self.assertEqual(get_data["code"], out_come["code"])
            result = "pass"
        except Exception as e:
            result = "FAIL"
            my_logger.error("测试结果报错为：{}".format(str(e)))
            raise e
        finally:
            BaseDef.write_back(test_case_path, get_data["sheet"], get_data["id"] + 1, 13, out_come['code'])
            BaseDef.write_back(test_case_path, get_data["sheet"], get_data["id"] + 1, 14, result)
            BaseDef.write_back(test_case_path, get_data["sheet"], get_data["id"] + 1, 23, str(out_come))
            my_logger.info("结果已写回")

        '''——————判断是否需要对比期望——————'''
        if get_data["expected"]:
            expected = eval(get_data["expected"])
            if expected["expected_type"] == 1:  # 对比预期值  和 data的对应参数值  是否一致
                expected_res = Compare().compare_expected(expected["target"][0],
                                                          out_come["data"][expected["target"][1]])
            elif expected["expected_type"] == 2:  # 判断outcome的data不为空
                expected_res = Compare().exist_expected(out_come)
            elif expected["expected_type"] == 3:  # 对比msg是否正确
                expected_res = Compare().exist_msg(expected["msg"], out_come["msg"])
            else:                                 # 判断outcome的data为空 ==4
                expected_res = "pass" if Compare().exist_expected(out_come) == "FAIL" else "FAIL"

            try:
                self.assertEqual("pass", str(expected_res))
            except Exception as e1:
                raise e1
            finally:
                BaseDef.write_back(test_case_path, get_data["sheet"], get_data["id"] + 1, 19, expected_res)

        '''——————判断是否需要对比数据库——————'''
        if get_data["check_sql"]:
            check_sql = get_data["check_sql"]
            my_logger.info("sql语句是：{}".format(check_sql))
            sql_database = eval(check_sql)["database"] if "database" in check_sql else ""
            check_res = ""
            if "sql_type" in check_sql:
                if eval(check_sql)["sql_type"] == 4:  # 查询结果存在
                    check_res = Compare().exist_mysql(eval(check_sql)["sql"], get_data["init_path"], sql_database)
                    check_res = "pass" if check_res != "FAIL" else "FAIL"
                elif eval(check_sql)["sql_type"] == 3:  # 查询结果不存在
                    check_result = Compare().exist_mysql(eval(check_sql)["sql"], get_data["init_path"], sql_database)
                    check_res = "pass" if check_result == "FAIL" else "FAIL"
                elif eval(check_sql)["sql_type"] == 2:  # 查询结果和data长度比对
                    my_logger.info("对比数据长度为：{}".format(str(len(out_come["data"]))))
                    check_res = Compare().compare_mysql(
                        eval(check_sql)["sql"], len(out_come["data"]), get_data["init_path"], sql_database)
                elif eval(check_sql)["sql_type"] == 1:  # 查询结果是否存在，并返回查询结果
                    check_res = Compare().exist_mysql(eval(check_sql)["sql"], get_data["init_path"], sql_database)
                    if check_res != "FAIL":
                        my_logger.info("check_res值：{}".format(check_res))
                        # ——————————下面进行sql返回值的处理————————————
                        returned_value = eval(get_data["returned_value"])
                        for j in range(len(returned_value)):
                            returned_single = returned_value[j]
                            if type(getattr(init_path, returned_single)) == list:
                                getattr(init_path, returned_single).append(check_res[j])
                            else:
                                setattr(init_path, returned_single, check_res[j])
                        # ——————————————————————————————————————————

            if "expected" in check_sql:  # 如果存在expected，查询结果和期望值比对
                my_logger.info("期望值{}".format(eval(check_sql)["expected"]))
                if "password" in check_sql:
                    expected_data = BaseDef().md5ing(eval(check_sql)["expected"])
                else:
                    expected_data = eval(check_sql)["expected"]
                check_res = Compare().compare_mysql(
                    eval(check_sql)["sql"], expected_data, get_data["init_path"], sql_database)

            try:
                self.assertNotEqual("FAIL", str(check_res))
            except Exception as e2:
                raise e2
            finally:
                BaseDef.write_back(test_case_path, get_data["sheet"], get_data["id"] + 1, 17, str(check_res))

        my_logger.info("*****{}测试结束了*****".format(get_data["case_name"]))

    def tearDown(self):
        pass
