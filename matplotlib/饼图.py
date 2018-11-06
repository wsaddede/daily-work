import matplotlib.pyplot as plt
import numpy as np

# 解决中文不显示问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决保存图片是负号‘-’ 显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

data = np.load('国民经济核算季度数据.npz')
name = data['columns']
values = data['values']

plt.figure(figsize=(6, 6))  # 将画布设成正方形
label = ['第一产业', '第二产业', '第三产业']
# explode 半径
explode = [0.01, 0.01, 0.01]  # 设定各项距离圆心的半径
plt.pie(values[-1, 3:6], explode=explode, labels=label, autopct='%1.1f%%')

plt.show()