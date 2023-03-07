# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 20:21
# @Author  : Jeico
# @File    : run_single.py

import unittest
from tools import HTMLTestRunnerNew
from tools.test_http import TestHttp
from conf.environment_config import EnvironmentConfig

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttp))


# 执行
test_report_path = EnvironmentConfig.test_report_path
with open(test_report_path, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='API自动化测试报告',
                                              description='本报告路径为：{}，测试情况如下：'.format(str(test_report_path)),
                                              tester='测试组')
    runner.run(suite)
