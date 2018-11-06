import requests,json

for i in range(1,6):
    url = 'https://www.creditchina.gov.cn/api/credit_info_search?keyword=%E6%95%99%E8%82%B2&templateId=&page={}&pageSize=10'.format(i)
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
    req = requests.get(url=url,headers=headers).content.decode('utf-8')
    #print(req)
    obj = json.loads(req)
    #print(obj)
    for j in range(0,10):
        sort = obj['data']['results'][j]
        name = sort['name']
        ids = sort['idCardOrOrgCode']
        good = sort['goodCount']
        bad = sort['badCount']
        dishonesty = sort['dishonestyCount']
        others = sort['otherCount']
        print(name,ids,good,bad,dishonesty,others)
