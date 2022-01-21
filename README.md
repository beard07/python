pyhton
===
爬虫笔记
---
* 基础请求<br>
request | urlopen方法 最直接的get请求方式

```python
import urllib.request
response = urllib.requset.urlopen(url,data=None,[timeout]*)
print(response.read().decode('utf-8'))
```
urllib.requset.urlopen([url](/ "网页链接"), [data=None](/ "请求携带的数据，比如用户名和密码"), [timeout](/ "请求超时时间"))<br>
request | Request方法 可以加入自定义headers数据 
```
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
