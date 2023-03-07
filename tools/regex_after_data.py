# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 15:09
# @Author  : Jeico
# @File    : regex_after_data.py
import re
from tools.base_def import BaseDef


class AfterDataRegex:

    @staticmethod
    def after_data_regex(s, init_data):
        """————通过正则完成数据的替换和参数化,专门处理带*的————
            参数：
                s：需要替换的内容， str ；
                init_data：init文件的对应class名， class；
            返回：
                替换后的内容， str ；
        ————————————————————————————————————————————"""
        while re.search("\*{(.*?)}", str(s)):
            key = re.search("\*{(.*?)}", str(s)).group(0)
            value = re.search("\*{(.*?)}", str(s)).group(1)
            init_path = BaseDef().get_import(init_data)
            if init_data == "system_management_init":
                if value == "DictionaryName_no":
                    s = str(s).replace(key, str((getattr(init_path, "DictionaryName_nos"))[-1]))
                elif value == "DictionaryName_pno":
                    s = str(s).replace(key, str((getattr(init_path, "DictionaryName_nos"))[-2]))
                elif value == "DictionaryName_id":
                    s = str(s).replace(key, str((getattr(init_path, "DictionaryName_ids"))[-1]))
                elif value == "DictionaryName_pid":
                    s = str(s).replace(key, str((getattr(init_path, "DictionaryName_ids"))[-2]))
                else:
                    s = str(s).replace(key, str(getattr(init_path, value)))
            else:
                s = str(s).replace(key, str(getattr(init_path, value)))
        return s


