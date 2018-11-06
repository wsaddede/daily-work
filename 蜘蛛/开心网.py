from urllib import request,parse
from http import cookiejar
import ssl
#Cookie: _ref=5bbc0b14b5d9a; _cpmuid=1071869992; SERVERID=_srv80-122_; _vid=C82BF3E2C5F00001C74615CA3D9C1F1A; sessionloginid=93c6975034d6ad5f634fefbf9ada5072; _laid=0; _sso=logout; _user=793ee9c329f355867fa6cf4d6e1daf55_181794584_1539056035; _preemail=qq1316577073; _kx=MTgxNzk0NTg0OnpteTJ6a2ltMmczazo1YXQ0NHM2NDdyaTgyNWZod3g3ODUzZ2d1N2EyZDF6d3lpdjQ%3D; wizard_goto=%2Fkxmobile%2Faj_kxmobile_tip.php

ssl._create_default_https_context = ssl._create_unverified_context

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    base_url = 'https://security.kaixin001.com/login/login_post.php'
    data = {
        'email':'13554477478',
        'password':'221122'
    }
    data_enc = parse.urlencode(data).encode('utf-8')
    req = request.Request(url=base_url,data=data_enc,method='POST')
    response = opener.open(req)

def getHomepage():
    base_url = 'http://www.kaixin001.com/home/?uid=181794561'
    response = opener.open(base_url)
    html = response.read().decode('utf-8')
    with open('kaixin.html', 'w', encoding='utf-8')as f:
        f.write(html)


if __name__ == '__main__':
    login()
    getHomepage()
