pyhton
===
爬虫笔记
---
* 基础请求<br>
request | 最直接网页的请求方式

```python
import urllib.request
response = urllib.requset.urlopen(url,data=None,[timeout]*)
print(response.read().decode('utf-8'))
```
urllib.requset.urlopen([url](/ "网页链接"), [data=None](/ "请求携带的数据，比如用户名和密码"), [[timeout]*](/ "请求超时时间"))<br>

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
