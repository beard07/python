import urllib.request
from urllib import request,parse
import ssl

#网页地址
url = 'http://www.zzz10.com/index/login/login.html'

#头信息
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0',
}

#请求的参数
dict = {
    'user_name': '4756045055',
    'user_pwd': '648198',
}

#把请求的参数转化为 byte
data = bytes(parse.urlencode(dict),'utf-8')

#封装 request
req = request.Request(url,data = data, headers = headers, method='POST')

#进行请求
response = request.urlopen(req)

print(response.read().decode('utf-8'))
