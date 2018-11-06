import requests,re

url = "https://api.bilibili.com/x/v1/dm/list.so"

querystring = {"oid":"45329552"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "27bdc269-626f-846e-c414-08612075ba12"
    }

response = requests.request("GET", url, headers=headers, params=querystring,verify=False)
# print(response.text)

alt = re.compile(r'>(.*?)</d>')
result1 = alt.findall(response.content.decode('utf-8'))
# print(result1)
# for item in result1:
#     print(item)
