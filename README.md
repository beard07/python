pyhton
# 爬虫笔记
## 基础请求
***
### Urllib 库
* request 模块 (用来发起请求)
  * [`urlopen`方法 | 最直接的get请求方式]()
  * [`Request`方法 | 可以加入自定义headers数据]()
* error 模块 (在使用`request`模块遇到错了，用它来进行异常处理)
* parse 模块 (用来解析我们的 URL 地址，比如解析域名地址啦，URL指定的目录等)
* robotparser 模块 (用来解析网站的 robot.txt)

### Requests 库
* [`get` 请求访问]()
* [`post` ]()
* [`put` 、 `delete` 、 `head` 、 `optins`]()
* [`text` 获取服务器响应文本内容]()
* [`content` 获取字节响应内容]()
* [`status_code` 获取响应码]()
* [`headers` 获取响应头]()
* [获取 socket 流响应内容]()
* ['json' 获取 json 响应内容]()
* [请求的时候用 json 作为参数]()
* [上传文件]()
* [获取 cookie 信息]()
* [发送 cookie 信息]()

### 正则表达式
* [常用符号]()
* re 库 正确使用正则表达式
  * [☞]() re.match 开头结尾全匹配
  * [☞]() re.search 匹配第一个结果
  * [☞]() re.findall 匹配所有匹配的结果
  * [☞]() re.sub 匹配所有内容并替换
  * [☞]() re.compile 匹配符封装


***
## Urllib 库
### request 模块
#### urlopen 最直接的get请求方式
`url`网页地址  `data`请求数据类似用户名密码  `timeout`请求超时时间
```python
import urllib.request
response = urllib.requset.urlopen(url,data=None,[timeout]*)
print(response.read().decode('utf-8'))
```
#### Request 可以加入自定义headers数据 
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
## Requests 库 需要ipi安装
```python
import requests
```
#### get命令
```python
#直接访问
r = requests.get('https://www.baidu.com')

#携带参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

#携带headers信息，假装自己是浏览器
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
```

#### post命令 可以添加多个值
```python
#直接post
r = requests.post('https://www.baidu.com', data = {'key':'value'})

#当你想要一个键里面添加多个值的时候
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r1.text) 
#{  ...  "form": {    "key1": [      "value1",      "value2"    ]  },  ...}
r1.text == r2.text 
#True
```

#### 其它乱七八糟的 Http 请求
```python
r = requests.put('https://httpbin.org/put', data = {'key':'value'})

r = requests.delete('https://httpbin.org/delete')

r = requests.head('https://httpbin.org/get')

r = requests.options('https://httpbin.org/get')
```
#### text命令  获取服务器响应文本
```python
r = requests.get('https://api.github.com/events')
r.text  #u'[{"repository":{"open_issues":0,"url":"https://github.com/...
r.encoding #'utf-8'
```

#### content 获取字节响应内容
```python
r.content #b'[{"repository":{"open_issues":0,"url":"https://github.com/...
```
#### status_code 获取响应码
```python
r = requests.get('https://www.baidu.com')
r.status_code #200
```
#### headers 获取响应头
```python
r.headers
  #{    
  #    'content-encoding': 'gzip',    
  #    'transfer-encoding': 'chunked',  
  #    'connection': 'close',    
  #    'server': 'nginx/1.0.4',    
  #    'x-runtime': '148ms',    
  #    'etag': '"e1ca502697e5c9317743dc078f67693f"',   
  #    'content-type': 'application/json'

  #}
```
#### 获取 socket 流响应内容
```python
r = requests.get('https://api.github.com/events', stream=True)
r.raw #<urllib3.response.HTTPResponse object at 0x101194810>
r.raw.read(10)  
#'x1fx8bx08x00x00x00x00x00x00x03'
```
#### json 获取 Json 响应内容
```python
r = requests.get('https://api.github.com/events')
r.json()
#[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
```
#### 请求的时候用 json 作为参数
```python
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
```
#### 上传文件
```python
url = 'https://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
r.text   
#{  ...  "files": {    "file": "<censored...binary...data>"  },  ...}
```
#### 获取 cookie 信息
```python
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']  
#'example_cookie_value'
```
#### 发送 cookie 信息
```python
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text  
#'{"cookies": {"cookies_are": "working"}}'
```
#### 设置超时
```python
requests.get('https://github.com/', timeout=0.001)
#Traceback (most recent call last):   File "<stdin>", line 1, in <module>requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)
```
***
## 正则表达式
#### 常用符号 https://c.runoob.com/front-end/854/

代码 | 	说明
------- | -------
.  |  - 除换行符、回车符以外的所有字符。
^  |  - 字符串开头。
$  |  - 字符串结尾。
\d, \w, \s  |  - 匹配 数字、 字符、 非空格。
\D, \W, \S  |  - 匹配 非数字、 非字符、 非空格。
\n, \r, \f, \t, \s  |  -匹配 换行、 回车、 换页、 TAB、 所有空白字符
?  |  - 0 次或 1 次匹配。
\*  |  - 匹配 0 次或多次。
\+  |  - 匹配 1 次 或多次。
[abc]  |  - 匹配 a、b、c 中的一个字母。
[a-z]  |  - 匹配 a 到 z 中的一个字母。
[^abc]  |  - 匹配除了 a、 b 或 c 中的其他字母。
aa\|bb | - 匹配 aa 或 bb。
{n}  |  -匹配 n 次。
{n,}  |  -匹配 n 次以上。
{m,n}  |  -最少 m 次，最多 n 次匹配。
(expr)  |  - 捕获 expr 子模式，ci
(expr)  |  - 捕获 expr 子模式,以 \1 使用它。
(?:expr)  |  - 忽略捕获的子模式。
(?=expr)  |  - 正向预查模式 expr。
(?!expr)  |  - 负向预查模式 expr。
( )  |  - 匹配括里面的内容
## re 库
#### re.match 开头结尾全匹配
```python
import re

content = 'Xiaoshuaib has 100 bananas'
#非贪婪匹配不加"?"，只出一个结果
res = re.match('^Xi.*(\d+).*s$',content)
print(res.group(1))
#0

#贪婪匹配加"?"，匹配所有
res = re.match('^Xi.*(\d+).*s$',content)
print(res.group(1))
```
#### re.S 忽略换行符进行匹配
```python
content = """Xiaoshuaib has 100 
bananas"""

res = re.match('^Xi.*?(\d+).*s$',content,re.S)
print(res.group(1))
```
#### re.search 匹配第一个结果
```python
content = """Xiaoshuaib has 100 
bananas"""

res = re.search('Xi.*?(\d+).*s',content,re.S)
print(res.group(1))
```
#### re.findall 匹配所有匹配的结果
```python
content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""

res = re.findall('Xi.*?(\d+).*?s;',content,re.S)
print(res)
```

#### re.sub 匹配所有内容并替换
```python
content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""

content = re.sub('d+','250',content)
print(content)
```
#### re.compile 匹配符封装 便于重复使用
```python
content = "Xiaoshuaib has 100 bananas"

pattern = re.compile('Xi.*?(\d+).*s',re.S)
res = re.match(pattern,content)
#和 res = re.match('^Xi.*?(d+)s.*s$',content,re.S) 是一样的
print(res.group(1))
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
