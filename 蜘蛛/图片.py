import requests
url = 'http://langlang2017.com/img/logo.png'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
content = requests.get(url=url,headers=headers)

with open ('logo.png','wb')as f:
    f.write(content.content)