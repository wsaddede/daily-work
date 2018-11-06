import requests
from bs4 import BeautifulSoup

url = 'http://langlang2017.com'
response = requests.get(url=url).content.decode('utf-8')

##转换页面格式
soup = BeautifulSoup(response,'lxml')

#获取标签，返回的是第一个符合条件额标签
#a=soup.title

#标签名字
#print(soup.meta.name)

#属性提取--返回字典形式:
#print(soup.meta.attrs)

#获取标签内容
#print(soup.title.string)

#获取子节点
# print(soup.head.contents)
#
# print(soup.body.children)

# print(soup.body.descendants)
