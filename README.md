pyhton
爬虫笔记
===
基础请求
---
***
* Urllib 库 (python内置)
   * error 模块 (在使用`request`模块遇到错了，用它来进行异常处理)
   * parse 模块 (用来解析我们的 URL 地址，比如解析域名地址啦，URL指定的目录等)
   * robotparser 模块 (用来解析网站的 robot.txt)
   * request 模块 (用来发起请求)
      * [urlopen方法 | 最直接的get请求方式]()
      * [Request方法 | 可以加入自定义headers数据]()
    
--
***
Urllib 库
===
***
request | urlopen方法 最直接的get请求方式
---
`url`网页地址  `data`请求数据类似用户名密码  `timeout`请求超时时间
```python
import urllib.request
response = urllib.requset.urlopen(url,data=None,[timeout]*)
print(response.read().decode('utf-8'))
```
request | Request方法 可以加入自定义headers数据 
---
```python
from urllib import request,parse

#定义一下我们的请求 url 和 header
url = 'https://biihu.cc//account/ajax/login_process/'
headers = {
    #需要使用Fiddler工具获取headers信息，假装自己是浏览器
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

#定义一下我们的请求参数
dict = {
    'return_url':'https://biihu.cc/',
    'user_name':'xiaoshuaib@gmail.com',
    'password':'123456789',
    '_post_type':'ajax',
}

#把请求的参数转化为 byte
data = bytes(parse.urlencode(dict),'utf-8')
#封装 request 
req = request.Request(url,data=data,headers=headers,method='POST')
#最后我们进行请求
response = request.urlopen(req,context=context)
print(response.read().decode('utf-8'))
```
***
Requests 库 需要ipi安装
===
```python
import requests

#get命令
r = requests.get('https://www.baidu.com')

#post命令
r = requests.post('https://www.baidu.com', data = {'key':'value'})

#其它乱七八糟的 Http 请求
r = requests.put('https://httpbin.org/put', data = {'key':'value'})

r = requests.delete('https://httpbin.org/delete')

r = requests.head('https://httpbin.org/get')

r = requests.options('https://httpbin.org/get')

#携带参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

#携带headers信息，假装自己是浏览器
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

#获取服务器响应文本
r = requests.get('https://api.github.com/events')
r.text  #u'[{"repository":{"open_issues":0,"url":"https://github.com/...
r.encoding #'utf-8'

#获取字节响应内容
r.content #b'[{"repository":{"open_issues":0,"url":"https://github.com/...

#获取响应码
r = requests.get('https://www.baidu.com')
r.status_code #200

#获取响应头
r.headers

#获取 Json 响应内容
r = requests.get('https://api.github.com/events')
r.json()

#获取 socket 流响应内容
r = requests.get('https://api.github.com/events', stream=True)
r.raw #<urllib3.response.HTTPResponse object at 0x101194810>
r.raw.read(10)  #'x1fx8bx08x00x00x00x00x00x00x03'

#Post请求 当你想要一个键里面添加多个值的时候
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r1.text) #{  ...  "form": {    "key1": [      "value1",      "value2"    ]  },  ...}
r1.text == r2.text #True

#请求的时候用 json 作为参数
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)

#上传文件
url = 'https://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
r.text   #{  ...  "files": {    "file": "<censored...binary...data>"  },  ...}

#获取 cookie 信息
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']  #'example_cookie_value'

#发送 cookie 信息
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text  #'{"cookies": {"cookies_are": "working"}}'

#设置超时
requests.get('https://github.com/', timeout=0.001)
#Traceback (most recent call last):   File "<stdin>", line 1, in <module>requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)
```
大标题
===
中标题
---
***
普通文本用/<br>
`高亮文本`<br>
[文本超链接]()<br>
[文本超链接](/guodongxiaren "悬停显示")悬停显示<br>
***
* 一级圆点(星号后面有空格)
  * 二级圆点(前面+TAB)
    * 三级圆点 

>数据结构  
>>树  
>>>二叉树  
>>>>平衡二叉树  
>>>>>满二叉树  
***
插入图片<br>
![baidu](http://www.baidu.com/img/bdlogo.gif "百度logo") 
<br>插入项目中的图片https://github.com/guodongxiaren/ImageCache/raw/master/Logo/foryou.gif
***
插入代码片段
```python
print('使用3个1旁边的引号')
```
