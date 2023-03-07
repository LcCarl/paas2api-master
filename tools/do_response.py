# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 10:51 上午
# @Author  : Jeico
# @File    : do_response.py

from tools.base_def import BaseDef


class DoResponse:
    @staticmethod
    def do_response(data, test_case_path):
        """——————从response中获取参数值——————
        参数：
            data：T列中的内容， str  ； test_case_path： 对应的测试用例路径 ，str ；
        返回：
            根据传入参数，返回相应的匹配结果；
            当data传入多个：返回list；  当data传入一个，返回值  str；
            ————————————————————————————————————————————————————————"""
        if data.find(",") != -1:
            data_new = data.split(",")
            item_data = []
            for item in data_new:
                result = BaseDef().split_data(item)
                excel_data = BaseDef().read_excel(test_case_path, result[0], eval(result[1]) - 1, 22)
                result_data = BaseDef().get_depend_data(excel_data, result[2])
                item_data.append(result_data)
        else:
            result = BaseDef().split_data(data)
            excel_data = BaseDef().read_excel(test_case_path, result[0], eval(result[1]) - 1, 22)
            item_data = BaseDef().get_depend_data(excel_data, result[2])
        return item_data

