import matplotlib.pyplot as plt
import numpy as np

# 解决中文不显示问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决保存图片是负号‘-’ 显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

data = np.load('国民经济核算季度数据.npz')
name = data['columns']
values = data['values']

plt.figure(figsize=(6, 5))
plt.bar(range(3), values[-1, 3:6], width=0.5)
label = ['第一产业', '第二产业', '第三产业']
plt.xlabel('产业')
plt.ylabel('生产总值（亿元）')
plt.title('2017年第一季度各产业国民生产总值')
plt.xticks(range(3), label)

# 显示出直方图y值
for x, y in zip(range(3), values[-1, 3:6]):
    plt.text(x, y, y, ha='center', fontsize=10)


plt.show()
