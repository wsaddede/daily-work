from urllib import request,parse
import json
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

req = request.Request(url=url,headers=headers)

response = request.urlopen(req).read().decode('utf-8')

obj = json.loads(response)

res = ''
for item in obj['subjects']:
    res += '电影名字：' + item['title'] +'      地址：'+ item['url'] + '\n'
print(res)