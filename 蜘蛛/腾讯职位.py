import requests
from lxml import etree
for i in range(0,81,10):
    url = 'https://hr.tencent.com/position.php?keywords=python&tid=0&lid=2156&start=' +'%d'%i+ '#a'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    req = requests.get(url=url,headers=headers)
    #print(req.url)

    tree = etree.HTML(req.content.decode('utf-8'))
    #print(tree)

    tr_list = tree.xpath('//table[@class="tablelist"]/tr')
    #print(len(tr_list))

    for tr in tr_list:
        name = tr.xpath('./td[1]/text()|./td[1]/a/text()')
        #print(name)
        nother = tr.xpath('./td/text()')
        #print(nother)
        info = name[0] +'+'+ nother[0] +'+'+ nother[1] +'+'+ nother[2]+'+'+ nother[3]+'\n'
        with open('tencent.txt','a+',encoding='utf-8')as f:
            f.write(info)