# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 10:57
# @Author  : Jeico
# @File    : compare.py

from tools.my_log import MyLog
from tools.do_mysql import DoMysql

my_logger = MyLog()


class Compare:

    @staticmethod
    def compare_mysql(sql=None, data=None, init_path="", database=""):
        """—————sql———查询结果  与  预期值  进行比对————————
            参数：
                sql:数据库查询语句   str；  data：需要与数据库进行比对的数据  str；
                init_path：如果需要根据这个值，查询对应的数据库，则需要填写   str；
            返回：相同pass，不同FAIL  ；  str
            ——————————————————————————————————"""
        check_res = ""
        if sql:
            my_logger.info("————此条用例需要进行数据库校验：是否相等——————")
            pass_time = 0
            try:
                mysql_data = DoMysql.do_mysql(sql, init_path=init_path, database=database)
                my_logger.info("****   mysql_data:{}   ****".format(str(mysql_data)))
                if str(data).find(",") != -1:
                    new_data = tuple(str(data).split(","))
                    my_logger.info("****   expected_data:{}   ****".format(str(new_data)))
                    for index, value in enumerate(mysql_data[0]):
                        if str(value) == new_data[index]:
                            pass_time += 1
                else:
                    my_logger.info("****   expected_data:{}   ****".format(str(data)))
                    if str(mysql_data[0][0]) == str(data):
                        pass_time += 1
                if len(mysql_data[0]) == pass_time:
                    check_res = "pass"
                    my_logger.info("****   校验通过   ****")
                else:
                    check_res = "FAIL"
                    my_logger.info("****   校验失败   ****")
            except Exception as e:
                check_res = "FAIL"
                my_logger.info("****   查询失败   ****")
                raise e
            finally:
                return check_res

    @staticmethod
    def exist_mysql(sql=None, init_path="", database=""):
        """————sql————判断查询结果是否存在————————
            参数：
                sql:数据库查询语句   str；
                init_path：如果需要根据这个值，查询对应的数据库，则需要填写   str；
            返回：
                若存在，则返回元组  Tuple；
                不存在则FAIL  str；
            ——————————————————————————————————"""
        check_res = ""
        if sql:
            my_logger.info("————此条用例需要进行数据库校验：是否存在，输出元组——————")
            try:
                mysql_data = DoMysql.do_mysql(sql, init_path=init_path, database=database)
                my_logger.info("sql查询的结果为：{}".format(mysql_data))
                check_res = mysql_data[0]
                my_logger.info("****   校验通过   ****")
            except Exception as e:
                check_res = "FAIL"
                my_logger.info("****   查询失败   ****")
                raise e
            finally:
                return check_res

    @staticmethod
    def compare_expected(expected=None, result=None):
        """—————response———预期结果 与 实际结果 进行比对——————————
            参数：
                expected：期望值 str； result：实际结果  str；
            返回：：相同pass，不同FAIL  ；  str
            ——————————————————————————————————"""
        if expected:
            my_logger.info("————此条用例需要进行期望值校验——————")
            my_logger.info("期望值是：{}".format(expected))
            my_logger.info("实际值是：{}".format(result))
            if str(expected) == str(result):
                check_res = "pass"
                my_logger.info("****   校验通过   ****")
            else:
                check_res = "FAIL"
                my_logger.info("****   校验失败   ****")
            return check_res

    @staticmethod
    def exist_expected(result=None):
        """——————response——————data内容不为空————
            参数：   result：实际结果   dic；
            返回：   data有值pass，没值FAIL  ；  str
            ———————————————————————————————————————— """
        if result:
            my_logger.info("————此条用例需要校验查询结果是否存在——————")
            # my_logger.info("实际值是：{}".format(result))
            if str(result).find("null") != -1:
                result_str = str(result).replace("null", "None")
                if eval(result_str)["data"]:
                    check_res = "pass"
                    my_logger.info("****   校验通过   ****")
                else:
                    check_res = "FAIL"
                    my_logger.info("****   校验失败   ****")
            else:
                if result["data"]:
                    check_res = "pass"
                    my_logger.info("****   校验通过   ****")
                else:
                    check_res = "FAIL"
                    my_logger.info("****   校验失败   ****")
            return check_res

    @staticmethod
    def exist_msg(expected=None, result=None):
        """—————response：msg———预期结果 与 msg中的结果 进行比对——————
            参数：
                expected：期望值 str； result：msg实际结果  str；
            返回：：相同pass，不同FAIL  ；  str
            ——————————————————————————————————"""
        if expected:
            my_logger.info("————此条用例需要进行msg校验——————")
            my_logger.info("期望值是：{}".format(expected))
            my_logger.info("实际值是：{}".format(result))
            if expected in result:
                check_res = "pass"
                my_logger.info("****   校验通过   ****")
            else:
                check_res = "FAIL"
                my_logger.info("****   校验失败   ****")
            return check_res

