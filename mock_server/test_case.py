
import unittest
import requests
import json

class MyTestCase(unittest.TestCase):
    def test_case001(self):
        # 1,定义所需请求的URL，和参数
        url="http://apis.juhe.cn/mobile/get"
        pay_load={
            "phone":"13419591290",
            "key":"802831374e480e92f88f1bd989a805b0"
        }
        #2，通过requests发送一个get请求
        resp=requests.get(url,params=pay_load)
        # 3，设置HTTP响应内容的而字符编码，
        resp.encoding="utf-8"
        # 4，获取http响应的内容
        resp_text=resp.text
        # 5，将符合字典格式的字符串，转换成json字典
        resp_json=json.loads(resp_text)
        print (resp_json['resultcode'])
        # 如果响应的返回值为json,识别：响应的header中包括Content-Type:application/json
        # 使用resp.json直接俄获取json格式字典
        resp_jsondata=resp.json()
        print(resp_jsondata['reason'])

        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
