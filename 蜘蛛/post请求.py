from urllib import request, parse
import json


# https://translate.google.cn
# word = input('请输入单词：')

def Fanyi(word):
    # 接口地址
    url = 'https://fanyi.baidu.com/sug'

    # 表单数据
    data = {
        'kw': word
    }

    # 封装请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    # 处理表单数据
    data_str = parse.urlencode(data)

    # 封装请求对象
    req = request.Request(url=url, headers=headers, data=bytes(data_str, encoding='utf-8'))

    # 发起网络请求
    content = request.urlopen(req).read().decode('utf-8')

    # json格式字符串转换成python对象（列表，字典）
    obj = json.loads(content)
    res = ''
    for item in obj['data']:
        res += item['v'] + '\n'
    return res


if __name__ == '__main__':
    while True:
        words = input('请输入单词：')
        content = Fanyi(words)

        print(content)
