import requests,re

response = requests.get('http://langlang2017.com/')
# pattern = re.compile(r'<div class="banner_box">[\s\S]*?</div>')
# result = pattern.findall(response.content.decode('utf-8'))
# new_pattern = re.compile(r'alt="(.*)"\ssrc="(.*)"')
# new_result = new_pattern.findall(result[0])
# print(new_result)

alt = re.compile(r'alt="(.*)"\ssrc="(.*)"')
result1 = alt.findall(response.content.decode('utf-8'))
print(result1)

http = re.compile(r'href="(https?.*?)"')
result2 = http.findall(response.content.decode('utf-8'))
print(result2)

beian = re.compile(r'class="beian">(.*)<a')
result3 = beian.findall(response.content.decode('utf-8'))
print(result3)


