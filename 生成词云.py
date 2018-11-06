from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

# 背景图
backgroup = plt.imread('./22.jpg')
# 读生成词云的文档
f = open('./danmu.txt', 'r', encoding='utf-8').read()

wordcloud = WordCloud(
    background_color='white',  # 设置背景颜色 ，默认黑色
    mask=backgroup,  # 笼罩图
    font_path=r'‪C:\Windows\Fonts\simsun.ttc',
    #width=1000,
    #height=100,
    #margin=2,  # 边缘宽度
    #max_words=200,
    #min_font_size=15,



).generate(f)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
