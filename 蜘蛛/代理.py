from urllib import request
import random
{'http/https':'ip:端口'}
proxy_list = [
    {'https':'106.75.164.15:3128'},
    {'http':'175.148.79.87:1133'}
]
proxy_chose = random.choice(proxy_list)
proxy_hander = request.ProxyHandler(proxy_chose)
opener = request.build_opener(proxy_hander)
content = opener.open('http://langlang2017.com').read().decode('utf-8')
print(content)