# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 15:38
# @Author  : Jeico
# @File    : my_log.py
import logging
import time
from tools.project_path import *


class MyLog:

    @staticmethod
    def my_log(level, msg):
        """——————此方法被下面方法调用————————"""
        my_logger = logging.getLogger("jeico")
        my_logger.setLevel("DEBUG")
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-日志信息:%(message)s')

        # 创建控制台
        ch = logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)

        # 创建文件
        curTime = time.strftime("%Y-%m-%d %H", time.localtime())
        fh = logging.FileHandler(test_logs_path + "/API_Test_{0}.log".format(curTime), encoding='UTF-8')
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)

        # 添加一个渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)
        elif level == 'EXCEPTION':
            my_logger.exception(msg)

        # 关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    """——————以下方法作为对外可调用方法——————
    参数：msg：要输出的日志内容   str； 
    ——————————————————————————————————"""
    def debug(self, msg):
        self.my_log("DEBUG", msg)

    def info(self, msg):
        self.my_log("INFO", msg)

    def warning(self, msg):
        self.my_log("WARNING", msg)

    def error(self, msg):
        self.my_log("ERROR", msg)

    def critical(self, msg):
        self.my_log("CRITICAL", msg)

    def exception(self, msg):
        self.my_log("EXCEPTION", msg)

