import requests
#创建一个session对象
session = requests.session()

#发起第一次请求：
url = 'http://www.renren.com/PLogin.do'

data = {
    'email':'17344411240',
    'password':'QQ2849464'
}
session.post(url=url,data=data)

#发起第二次请求
response = session.get(url='http://www.renren.com/968293395/profile')

#保存
with open('renrenhome.html','w',encoding='utf-8')as f:
    f.write(response.text)
    
    
