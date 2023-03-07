# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 11:42
# @Author  : Jeico
# @File    : regex_before_data.py
import re
from tools.base_def import BaseDef


class BeforeDataRegex:

    @staticmethod
    def before_data_regex(s, init_data):
        """————通过正则完成数据的替换和参数化,专门处理带$的————
            参数：
                s：需要替换的内容， str ；
                init_data：init文件的对应class名， class；
            返回：
                替换后的内容， str ；
                如果是add_data，保存对应的cur值并更新此参数；
        ————————————————————————————————————————————"""
        while re.search("\${(.*?)}", str(s)):
            key = re.search("\${(.*?)}", str(s)).group(0)
            value = re.search("\${(.*?)}", str(s)).group(1)
            s = str(s).replace(key, str(getattr(init_data, value)))
            if s.find("add_data") != -1:
                mid_data = eval(s)["add_data"]
                if mid_data is not None:
                    add_data = eval(mid_data)
                    for i in add_data:
                        if value == i:
                            setattr(init_data, value + "_cur", getattr(init_data, value))
                            if i == "Email":
                                setattr(init_data, value, BaseDef().get_email())
                            elif i == "Phone":
                                setattr(init_data, value, BaseDef().get_phone())
                            else:
                                setattr(init_data, value, BaseDef().time_stamp()())
        return s


