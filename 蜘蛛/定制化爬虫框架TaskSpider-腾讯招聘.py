
import requests
from bs4 import BeautifulSoup
import threading
from queue import Queue#引用队列
import time

#创建线程的两种方式：
#方法1：创建一个类，需要继承Thread类，并且覆写run方法
class Thread_crawl(threading.Thread):
    """
    获取页面信息线程,生产者
    """
    def __init__(self,name,page_queue):
        threading.Thread.__init__(self)
        self.name = name
        #拿到了任务队列
        self.q = page_queue

    def run(self):
        while True: #要一起去劳动，不能偷懒（出现的问题是只做了一个任务就休息了）

            if self.q.empty():
                break
            else:
                #从任务队列当中取出还没有被爬的页码
                page = self.q.get()
                print(self.name,'---star-页码是：',page)

                url ='https://hr.tencent.com/position.php?&start=%d#a'%((page-1)*10)
                print(url)
                self.get_content(url=url)
                print(self.name,'---end 页码是：',page)


    #一、获取页面信息
    def get_content(self,url):
        #网络访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        #如果网络请求不成功，最多重试4次
        timeout = 4
        while True:
            if timeout<=0:
                break

            try:
                response = requests.get(url=url,headers=headers,verify=False)

                #将获取的页面存到“页面待解析的队列”当中去
                content_q.put(response.text)

                break#只要成功一次就跳出循环
            except:
                print('丢失一次机会，timeout:',timeout)
                timeout-=1 #丢失一次机会

#消费者线程
class Thread_customer(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        while not flag:
            #解析线程什么时候退出问题：
            #(1)所有页面都获取到了 and（2）待解析队列为空
            #page_queue.empyt()不可以

            try:
                content = content_q.get(block=False)
                print('%s-----star-----'%self.name)
                self.get_data(content)
                print('%s-----end-------'%self.name)
            except:
                pass


    #二、数据提取
    def get_data(self,content):
        soup = BeautifulSoup(content,'lxml')

        tr_list = soup.find_all('tr')

        #去除非数据tr元素--第1个元素和倒数2个元素
        tr_list.pop()#默认从列表的尾部删除一个数据
        tr_list.pop()
        tr_list.pop(0)#去除表头

        for tr in tr_list:
            td_list = tr.select('td')
            #名称
            name = td_list[0].select('a')[0].get_text()
            #职位类别
            type = td_list[1].get_text()
            #人数
            num = td_list[2].get_text()
            #地点
            place = td_list[3].get_text()

            #发布时间
            publish_time = td_list[4].get_text()

            #保存
            item = name+','+type+','+num+','+place+','+publish_time+'\n'
            with open('tencent.txt','a',encoding='utf-8') as fp:
                fp.write(item)

#"页面待解析队列"
content_q = Queue()

#获取页面线程都死光了标识
flag = False

if __name__ == '__main__':

    #页面待解析队列

    # 开始时间
    t_star = time.time()

    #用队列把任务和爬虫对象分离

    #步骤1：生成任务
    #把任务放到一个队列当中
    page_queue = Queue()
    for page in range(1,11,1):
        page_queue.put(page)

    #步骤2：生成线程--生产者
    crawls_name = ['producter1','producter2','producter3']
    crawls_thread = []
    for name in crawls_name:
        crawl = Thread_crawl(name,page_queue)
        crawl.start()
        crawls_thread.append(crawl)

    #消费者--
    customers_name=['customers1','customers2','customers3']
    for name in customers_name:
        #创建消费者线程
        customer = Thread_customer(name)
        customer.start()


    #为了保证下面的指定是在所有任务完成之后才被执行
    while not page_queue.empty():#page1,2,3,  page_queue.empty()结果False
        #not False---->True--->pass---判断
        #。。。。
        #page1,2,3,4,5,~10都被执行了，page_queue.empty()结果True
        #not True---->False---->条件为假，退出循环
        pass

    #阻塞线程---让子线程都执行完成之后，主线程再往下进行。
    for thread in crawls_thread:
        thread.join()

    #在上述代码之后，如果有代码被执行，则表示爬虫类线程都死了
    flag = True#页面信息线程们都死了

    print(content_q.qsize(),'flag')
    # 结束时间
    t_end = time.time()
    print('用时：%f（秒）'%(t_end-t_star))





