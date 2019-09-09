import unittest
import requests
import json

class MyTestCase(unittest.TestCase):

    def test_101(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "13419591290", "key": "802831374e480e92f88f1bd989a805b0"}

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

    def test_102(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1341959", "key": "802831374e480e92f88f1bd989a805b0"}

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

    def test_103(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "134195", "key": "802831374e480e92f88f1bd989a805b0"}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        json_data = json.loads(response.text)

        act_result=(json_data['resultcode'],json_data['reason'])
        exp_result=("200","Wrong phone number!")
        self.assertEqual(act_result, exp_result)

    def test_104(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "134195a", "key": "802831374e480e92f88f1bd989a805b0"}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        json_data = json.loads(response.text)

        act_result=(json_data['resultcode'],json_data['return'])
        exp_result=("200","Wrong phone number!")
        self.assertEqual(act_result, exp_result)

    def test_105(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "134195@", "key": "802831374e480e92f88f1bd989a805b0"}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        json_data = json.loads(response.text)

        act_result=(json_data['resultcode'],json_data['return'])
        exp_result=("200","Wrong phone number!")
        self.assertEqual(act_result, exp_result)

    def test_106(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "134195 ", "key": "802831374e480e92f88f1bd989a805b0"}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        json_data = json.loads(response.text)

        act_result=(json_data['resultcode'],json_data['return'])
        exp_result=("200","Wrong phone number!")
        self.assertEqual(act_result, exp_result)

    def test_107(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "AAAAAAA", "key": "802831374e480e92f88f1bd989a805b0"}

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
        exp_result=("200","Wrong phone number!")
        self.assertEqual(act_result, exp_result)

    def test_109(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1590317", "key": "802831374e480e92f88f1bd989a805b0"}

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
        exp_result=("200","河北")
        self.assertEqual(act_result, exp_result)

    def test_110(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1590322", "key": "802831374e480e92f88f1bd989a805b0"}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        json_data = json.loads(response.text)

        act_result=(json_data['resultcode'],json_data['result']['city'])
        exp_result=("200","保定")
        self.assertEqual(act_result, exp_result)

    def test_111(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1300710", "key": "802831374e480e92f88f1bd989a805b0"}

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
        exp_result=("200","山西")
        self.assertEqual(act_result, exp_result)

    def test_112(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1300710", "key": "802831374e480e92f88f1bd989a805b0"}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        json_data = json.loads(response.text)

        act_result=(json_data['resultcode'],json_data['result']['zip'])
        exp_result=("200","30000")
        self.assertEqual(act_result, exp_result)

    def test_113(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1300001", "key": "802831374e480e92f88f1bd989a805b0"}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        json_data = json.loads(response.text)

        act_result=(json_data['resultcode'],json_data['result']['city'])
        exp_result=("200","常州")
        self.assertEqual(act_result, exp_result)

    def test_114(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1370032", "key": "802831374e480e92f88f1bd989a805b0"}

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
        exp_result=("200","河北")
        self.assertEqual(act_result, exp_result)

    def test_115(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1370032", "key": "802831374e480e92f88f1bd989a805b0"}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        json_data = json.loads(response.text)

        act_result=(json_data['resultcode'],json_data['result']['city'])
        exp_result=("200","常州")
        self.assertEqual(act_result, exp_result)

    def test_116(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "13001710011", "key": "802831374e480e92f88f1bd989a805b0"}

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
        exp_result=("200","山东")
        self.assertEqual(act_result, exp_result)

    def test_117(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1300171", "key": "802831374e480e92f88f1bd989a805b0"}

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
        exp_result=("200","济南")
        self.assertEqual(act_result, exp_result)

    def test_118(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1315067", "key": "802831374e480e92f88f1bd989a805b0"}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        json_data = json.loads(response.text)

        act_result=(json_data['resultcode'],json_data['result']['city'])
        exp_result=("200","丽江")
        self.assertEqual(act_result, exp_result)

    def test_119(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1315067", "key": "802831374e480e92f88f1bd989a805b0"}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'uid': "1",
            'cache-control': "no-cache",
            'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
        }
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        json_data = json.loads(response.text)

        act_result=(json_data['resultcode'],json_data['result']['zip'])
        exp_result=("200","674100")
        self.assertEqual(act_result, exp_result)

    def test_120(self):
        url = "http://apis.juhe.cn/mobile/get"

        querystring = {"phone": "1310081", "key": "802831374e480e92f88f1bd989a805b0"}

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
        exp_result=("200","黑龙江")
        self.assertEqual(act_result, exp_result)

if __name__ == '__main__':
    unittest.main()
