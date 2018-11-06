from selenium import webdriver
from lxml import etree
import json,requests


#无界面浏览器
driver = webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
#页面请求:
driver.get('https://www.douyu.com/directory/all')
# print(driver.page_source)
# driver.find_element_by_id('J-pager')
tree = etree.HTML(driver.page_source)
zhi = tree.xpath('//div[@id="J-pager"]/a[10]/text()')
num = zhi[0]
print(num)

# for i in range(1,int(num)+1):
#     url = "https://www.douyu.com/gapi/rkc/directory/0_0/%d"%i
#     headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
#     }
#     response = requests.get(url=url, headers=headers)#content.decode('utf-8')
# #查看响应的编码方式
# #     print(response.encoding)
#     obj = json.loads(response)
#     res = ''
#     for item in obj['data']['rl']:
#         res += '房间名字：' + item['rn'] +'   主播：'+ item['nn']+'   分类：'+ item['c2name'] +'   热度：'+ str(item['ol'])+ '\n'
#     # print(res)
#     with open('dy-json.txt','a',encoding='utf-8')as f:
#             f.write(res)