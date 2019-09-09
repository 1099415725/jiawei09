# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/22   10:30
# 开发工具： PyCharm


import requests
import json
url = "http://apis.juhe.cn/mobile/get"

querystring = {"phone":"13419591290","key":"802831374e480e92f88f1bd989a805b0"}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"uid\"\r\n\r\n1\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'uid': "1",
    'cache-control': "no-cache",
    'Postman-Token': "9597ca13-e388-436e-b335-60e82cddbc22"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
print(type(response.text))
json_data=json.loads(response.text)
print(type(json_data))
print(json_data['result']['province'])

