# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 15:43
# @Author  : Jeico
# @File    : do_mysql.py

import mysql.connector
from conf.environment_config import EnvironmentConfig
from tools.my_log import MyLog

my_logger = MyLog()


class DoMysql:
    @staticmethod
    def do_mysql(query, state="all", init_path="", database=""):
        """——————使用sql进行数据库查询————
            参数：
                query——查询语句  str；
                state——查询结果是1条还是多条，==1为一条，否则为多条。默认多条 ；
                init_path——data init的文件名，如果需要根据这个值，查询对应的数据库，则需要填写   str；
            返回：查询结果。列表嵌套元祖。
            ————————————————————————————————"""
        my_logger.info("——————进入数据库查询————————")
        db_config = EnvironmentConfig().db_config

        if database:
            db_config["database"] = database
        else:
            if EnvironmentConfig().environment_type == 5:
                if init_path in EnvironmentConfig().init_database.keys():
                    db_config["database"] = EnvironmentConfig().init_database[init_path]
        my_logger.info("——————db_config：{}————————".format(str(db_config)))

        cnn = mysql.connector.connect(**db_config)
        cursor = cnn.cursor()
        cursor.execute(query)

        if state == 1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()

        cursor.close()
        cnn.close()

        # 处理查询结果是bytes类型的情况
        result = []
        for i in res:
            list_item = []
            for j in i:
                if type(j) is bytes:
                    item = j.decode()
                    list_item.append(item)
                else:
                    list_item.append(j)
            result.append(tuple(list_item))

        return result


