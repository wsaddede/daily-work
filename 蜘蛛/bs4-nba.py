#球员名字 时间 篮板 助攻 得分  10页
import requests
from bs4 import BeautifulSoup
from openpyxl import workbook

wb = workbook.Workbook() #实例化
ws = wb.active #创建表
ws.append(['球员','时间','篮板','助攻','得分'])

for i in range(0,11):
    url='http://www.stat-nba.com/query.php?page=%d'%i+'&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=60#label_show_result'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    response=requests.get(url=url,headers=headers).content.decode('utf-8')
    soup=BeautifulSoup(response,'lxml')
    #print(soup)

    tr_list=soup.find_all('tr')

    tr_list.pop(0)
    #print(tr_list)

    for tr in tr_list:
        td_list=tr.select('td')
        #print(td_list)
        # 球员名字
        name=td_list[1].select('a')[0].get_text()
        #print(name)
        #时间
        time=td_list[4].text
        #print(time)
        #篮板
        lanban=td_list[14].text
        #rint(lanban)
        #助攻
        zhugong=td_list[17].text
        #print(zhugong)
        #得分
        defen=td_list[22].text
        #print(defen)

        # all='名字：'+name+' ,时间：'+time+' ,篮板：'+lanban+' ,助攻：'+zhugong+' ,得分：'+defen+'\n'
        # with open('nba.txt','a',encoding='utf-8')as fp:
        #     fp.write(all)
        ws.append([name+time+lanban+zhugong+defen])

wb.save('nba信息2.xlsx')