from urllib import request
import urllib

try:
    content = request.urlopen('http://www.langlang2017.com/abc.html')
    print(content)

#先抛子类异常
except urllib.error.HTTPError as e:
    print('HTTPError')

except urllib.error.URLError as e:
    print('URLError')