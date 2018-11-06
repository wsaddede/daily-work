# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.shanbay.com/wordlist//110521/232414/?page=1'
# response = requests.get(url=url).content.decode('utf-8')
# soup = BeautifulSoup(response,'lxml')

# words = soup.td.string
# print(words)



import requests
from bs4 import BeautifulSoup
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
for i in range(1,4):
    url='https://www.shanbay.com/wordlist//110521/232414/?page=%d'%i
    req=requests.get(url=url,headers=headers).content.decode('utf-8')
    soup=BeautifulSoup(req,'lxml')
    danci=soup.select('table .row')
    for j in range(0,len(danci)):
        danci_list=danci[j].select('td')
        english=danci_list[0].string
        chinese=danci_list[1].string
        cidan=english+':'+chinese+'\n'
        with open('扇贝.txt','a',encoding='utf-8')as fp:
            fp.write(cidan)
