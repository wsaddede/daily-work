from urllib import request,parse

url = 'http://www.renren.com/968293395/profile'

headers = {
    'Cookie': 'anonymid=jn11ic2vedbubc; depovince=BJ; jebecookies=6f150f34-c068-4d6c-8a54-999ec3442c36|||||; _r01_=1; ick_login=56eae9ec-e62c-4090-8b52-42a2193841fe; _de=4AA7A4E789A1EA6955A0BF36136018E8; p=ac0cc5dab9ab0ca839e57883a43e03eb5; ap=968293395; first_login_flag=1; ln_uact=17344411240; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=eabd03b9ff334a53ed23a4ff49b5dd8a5; societyguester=eabd03b9ff334a53ed23a4ff49b5dd8a5; id=968293395; xnsid=a9955897; loginfrom=syshome; wp_fold=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

#封装请求对象
req = request.Request(url=url,headers=headers)

#发起请求
content = request.urlopen(req).read().decode('utf-8')


with open('renren.html', 'w', encoding='utf-8')as fp:
    fp.write(content)