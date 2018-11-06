from urllib import request, parse


name = input('请输入贴吧名称：')

for page in range(1,11):

    url = 'http://tieba.baidu.com/f?'

    data = {
        'ie':'utf-8',
        'kw': name,
        'pn':(page-1)*50
    }

    data_enc = parse.urlencode(data)
    #parse功能：1.将文字进行解码；2.将多个参数用&连接；3.键与值用=连接

    new_url = url + data_enc

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    req = request.Request(url=new_url,headers=headers)

    content = request.urlopen(req).read().decode('utf-8')

    with open('%s第%d页.html'%(name,page), 'w', encoding='utf-8')as fp:
        fp.write(content)