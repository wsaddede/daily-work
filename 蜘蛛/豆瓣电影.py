from urllib import request,parse

# url = 'https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action='
# response = request.urlopen(url).read().decode('utf-8')
#
# with open('douban.html', 'w', encoding='utf-8')as fp:
#     fp.write(response)
pingjia = input('请输入好评率（5的倍数且相差10位，中间冒号分开）：')
begin = input('请输入起始页：')
over = input('请输入结束页：')
url = 'https://movie.douban.com/j/chart/top_list?'
data = {
    'type' : '11',
    'interval_id' : pingjia,
    'action' : '',
    'start' : begin,
    'limit' : over
}
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
data_enc = parse.urlencode(data)
new_url = url + data_enc
req = request.Request(url=new_url,headers=headers)
response = request.urlopen(req).read().decode('utf-8')

print(response)