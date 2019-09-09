# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/23   10:23
# 开发工具： PyCharm

import json
import unittest
import requests
from ddt import ddt,file_data
url = "http://apis.juhe.cn/mobile/get"


@ddt
class MyTestCase(unittest.TestCase):
    @file_data('file_data')
    def test_101(self,input_data):
        response = requests.request("GET", url,  headers=input_data["req_headers"], params=input_data['req_params'])

        exp_province=input_data['exp_result']['province']
        act_province=json.loads(response.text)['result']['province']
        self.assertEqual(exp_province, act_province,
                         "URL:%s,Params:%s,Exp_value:%s,Act_value:%s"%(url,input_data['req_params',exp_province,act_province]))

        exp_city = input_data['exp_result']['city']
        act_city = json.loads(response.text)['result']['city']
        self.assertEqual(exp_province, act_province,
                         "URL:%s,Params:%s,Exp_value:%s,Act_value:%s" % (url, input_data['req_params', exp_city, act_city]))

        exp_company = input_data['exp_result']['company']
        act_company = json.loads(response.text)['result']['company']
        self.assertEqual(exp_province, act_province,
                         "URL:%s,Params:%s,Exp_value:%s,Act_value:%s" % (url, input_data['req_params', exp_company, act_company]))