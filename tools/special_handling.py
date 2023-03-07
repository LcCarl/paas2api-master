# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 2:19 下午
# @Author  : Jeico
# @File    : special_handling.py

from tools.http_request import HttpRequest
from tools.do_mysql import DoMysql
from tools.my_log import MyLog
from data_init.common_data import CommonData
my_logger = MyLog()


class SpecialHandling:
    @staticmethod
    def camera_agent():
        """——————删除摄像头测点————————"""
        agent_code = CommonData.CameraAgentCode
        sql = 'SELECT agent_item_index FROM tb_agent_item WHERE agent_id=' \
              '(SELECT id FROM tb_agent WHERE protocol="camera" and agent_code="{}")'.format(agent_code)
        camera_agentItem = DoMysql().do_mysql(sql, init_path="service_agent_init")
        for i in camera_agentItem:
            my_logger.info("*****删除摄像头测点：{}*****".format(i[0]))
            api = "service-agent/agentItem/delete/camera/" + agent_code + "/" + i[0]
            HttpRequest().http_request_common("post", api, token=getattr(CommonData, "token"))


if __name__ == '__main__':
    SpecialHandling().camera_agent()
