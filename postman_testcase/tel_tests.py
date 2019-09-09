#encoding:utf-8

import unittest
import json
import  requests
from ddt import ddt,file_data


@ddt
class MyTestCase(unittest.TestCase):
    @file_data("test_tel.json")
    def test_101(self,phone):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": phone, "key": "802831374e480e92f88f1bd989a805b0"}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        json_data = json.loads(response.text)

        act_result=(json_data['resultcode'],json_data['result']['province'])
        exp_result=("200","湖北")
        self.assertEqual(act_result, exp_result)












if __name__ == '__main__':
    unittest.main()
