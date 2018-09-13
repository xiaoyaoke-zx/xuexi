#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
import urllib.request
import time
import requests

# 获取13位时间戳
stime = round(time.time()*1000)
print(stime)
# 拼接参数的另一种请求接口方式
param = {'mobile':'6007@dst','password':'MTIzLmNvbQ=='}
param1 = {'mobile':'6007@dst','password':'111111='}

http1 = requests.post('http://router.111yao.com/sltRouter?method=login',data=param)
http2 = requests.post('http://testrouter.111yao.com/sltRouter?method=login',data=param1)

if http2.status_code == 200:
    print("测试通过")
else:
    print("测试不通过")


# print(http1.text)
# print(http1.status_code)
#
# print('-----------------------------------')
#
# print(http2.text)
# print(http2.status_code)


#
# flag = False
# http1 = True
#
# if http1 == 1

# param1={'username':'test','password':'123456'}
#
#
# url = r'http://router.111yao.com/sltRouter?method=login&mobile=6007@dst&password=123.com'
#
# response = urllib.request.urlopen(url)
#
#
# html = json.loads(response.read())
#
# # print("题目:","《",html['title'],"》")
# print("题目:","《",html['title'],"》")