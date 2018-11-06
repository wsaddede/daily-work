from lxml import etree
import requests

for i in range(1,4):
    response = requests.get('https://www.shanbay.com/wordlist//110521/232414/?page=%d'%i)
    
    #转xml
    tree = etree.HTML(response.content.decode('utf-8'))

    #提取信息
    tr_list = tree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
    #print(len(tr_list))
    
    for tr in tr_list:
        #单词
        words = tr.xpath('./td/strong/text()')
        #翻译
        translate = tr.xpath('./td[2]/text()')

        info = words[0] +':'+ translate[0] + '\n'

        with open('words.txt','a+',encoding='utf-8')as f:
            f.write(info)