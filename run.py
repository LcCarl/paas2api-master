# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 4:23 下午
# @Author  : Jeico
# @File    : run.py

from tools.project_path import *
from tools.do_config import DoConfig

"""环境类型：
; 5——新的paas，测试环境 ；
"""

run_list = [5]

for i in run_list:
    DoConfig().set_config(run_path, "run_list", i)
    os.system("python3 run_single.py")
