import requests
response = requests.get(url='https://security.kaixin001.com/login/login_post.php',verify=False)
print(response.text)
