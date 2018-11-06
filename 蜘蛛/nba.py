#名字   时间   篮板  助攻   得分  
from selenium import webdriver
import time
from lxml import etree
from openpyxl import workbook

wb = workbook.Workbook() #实例化
ws = wb.active #创建表
ws.append(['球员','时间','篮板','助攻','得分'])

driver = webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
for i in range (0,11):
    driver.get('http://www.stat-nba.com/query.php?page=%d&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=60#label_show_result'%i)
    # with open('nba.html','w',encoding='utf-8')as f:
    #     f.write(driver.page_source)
    #re/bs4/xpath
    tree = etree.HTML(driver.page_source)

    nba_list = tree.xpath('//table[@class="stat_box"]/tbody/tr')
    # print(len(nba_list))

    for nba in nba_list:
        name = nba.xpath('./td/a[@class="query_player_name"]/text()')
        # print(name)
        times = nba.xpath('./td[5]/text()')
        # print(times)
        trb = nba.xpath('./td[15]/text()')
        # print(trb)
        ast = nba.xpath('./td[18]/text()')
        # print(ast)
        pts = nba.xpath('./td[23]/text()')
        # print(pts)
        # alls = '姓名:'+name[0]+','+'时间:'+times[0]+','+'篮板:'+trb[0]+','+'助攻：'+ast[0]+','+'得分:'+pts[0]+'\n'
        #with open('nba.txt','a+',encoding='utf-8')as f:
            #f.write(alls)
        ws.append([name[0],times[0],trb[0],ast[0],pts[0]])

wb.save('nba信息.xlsx')


