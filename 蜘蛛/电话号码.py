import requests,re

response = requests.get('http://langlang2017.com/')

#提取电话号码:
# pattern = re.compile(r'1[3|5|7|8|]\d{9}')
# result = pattern.findall(response.text)
# print(result)

#提取banner对应的src信息：
# pattern = re.compile(r'src="(.*)"')
# result = pattern.findall(response.text)
# print(result[2:6])  

pattern = re.compile(r'<div class="banner_box">[\s\S]*?</div>')
result = pattern.findall(response.content.decode('utf-8'))
#print(result)

new_pattern = re.compile(r'src="(.*)"')
new_result = new_pattern.findall(result[0])
print(new_result)

i=1
url = 'http://langlang2017.com/'
for src in new_result:
    full_url = url + src
    content = requests.get(full_url)
    #保存
    filename = 'banner%d.png'%i
    with open(filename,'wb')as f:
        f.write(content.content)
    i+=1