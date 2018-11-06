from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#无界面浏览器
driver = webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#页面请求:
driver.get('http://www.baidu.com')

#保存
# with open('baidu.html','w',encoding='utf-8')as f:
#     f.write(driver.page_source)

#页面截图
# driver.save_screenshot('baidu1.png')

#模拟窗口输入
driver.find_element_by_id('kw').send_keys('美女')
#driver.save_screenshot('baidu2.png')

#模拟点击
driver.find_element_by_id('su').click()
# time.sleep(5)#留出时间等待页面加载
# driver.save_screenshot('baidu3.png')

# print(driver.title)
# a = driver.find_element_by_id('wrapper').text
# print(a)

#获取cookies
# print(driver.get_cookies())

#模拟用户的键盘操作
#1.全选
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(5)
# driver.save_screenshot('baidu4.png')
#2.剪切
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
driver.save_screenshot('baidu5.png')