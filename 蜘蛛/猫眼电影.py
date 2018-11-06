import requests,re
from lxml import etree
url = 'http://maoyan.com/board'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
req = requests.get(url=url,headers=headers)
#contents = req.content.decode('utf-8')
# print(contents)
# pattern = re.findall(r'<i class="board-index board-index-\d+">(.*?)</i>[\d\D]*?<a href="(.*?)"\stitle="(.*?)"[\d\D]*?<p class="star">\n\s*([\d\D]*?)\s*</p>[\d\D]*?<p class="releasetime">(.*?)</p>[\d\D]*?<i class="integer">(.*?)</i>[\d\D]*?<i class="fraction">(.*?)</i>',contents)
# print(pattern)

#xml方法
tree = etree.HTML(req.content.decode('utf-8'))
tr_list = tree.xpath('//dl[@class="board-wrapper"]/dd')
#print(len(tr_list))

# for tr in tr_list:
#     rank = tr.xpath('./i[@class]/text()')
#     link = tr.xpath('./a/@href')
#     name = tr.xpath('./a/@title')
#     star = tr.xpath('.//p[@class="star"]/text()')
#     releasetime = tr.xpath('.//p[@class="releasetime"]/text()')
#     score1 = tr.xpath('.//i[@class="integer"]/text()')
#     score2 = tr.xpath('.//i[@class="fraction"]/text()')
#     #print(rank,link,name,star,releasetime,score1,score2)
    
#     info = rank[0]+','+link[0]+','+name[0]+','+star[0].strip()+','+releasetime[0]+','+score1[0]+score2[0]+'\n'
#     # print(info)
#     with open('movie.txt','a+',encoding='utf-8')as f:
#         f.write(info)
