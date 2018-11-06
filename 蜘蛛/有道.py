from urllib import request , parse
import hashlib
import time

salt = int(time.time()*1000)

word = input('请输入要翻译的单词：')

sign_str = "fanyideskweb" + word + str(salt) + "6x(ZHw]mwzX#u0V7@yfwK"

def getMd5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value,encoding='utf-8'))
    return md5.hexdigest()  #返回md5加密的字符串
sign = getMd5(sign_str)
print(sign)

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

data = {
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'false'
}

data_str = parse.urlencode(data)

len(data_str)

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': len(data_str),
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'P_INFO=wsaddede@vip.163.com|1538967628|0|mailvip|00&99|bej&1538141101&mailvip#bej&null#10#0#0|176080&0|mail163|wsaddede@vip.163.com; OUTFOX_SEARCH_USER_ID=-1012731839@10.168.1.8; JSESSIONID=aaaP15GoAuY7XgGelJxzw; OUTFOX_SEARCH_USER_ID_NCOO=1365191172.9017766; ___rl__test__cookies=1539072263230',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

req = request.Request(url=url, data=bytes(data_str, encoding='utf-8'), headers=headers)

content = request.urlopen(req).read().decode('utf-8')

print(content)
