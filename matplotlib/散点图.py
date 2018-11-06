import matplotlib.pyplot as plt
import numpy as np

# 解决中文不显示问题
plt.rcParams['font.sans-serif'] = 'SimHei'
# 解决保存图片是负号‘-’ 显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

data = np.load('国民经济核算季度数据.npz')
name = data['columns']
values = data['values']
print(values)

# 创建一个空白画布
# plt.figure(figsize=(8, 8), dpi=80)
#
# # 绘制散点图
# x = values[:, 0]
# y = values[:, 3]
#
# plt.scatter(x, y, marker='o', color='r')
# plt.scatter(x, values[:, 4], marker='o', color='b')
# plt.scatter(x, values[:, 5], marker='o', color='c')
# plt.xlabel('年份')
# plt.ylabel('生产总值(亿元)')
# plt.title('2000-2017年各季度各产业生产总值散点图')
# # xticks(给定需要放刻度名称的位置,刻度名称)
# plt.xticks(values[::4, 0], values[::4, 1], rotation=45)
#
# plt.legend(['第一产业', '第二产业', '第三产业'])
# plt.show()

######################2000年第一季度到2017年第一季度建筑业对比
######################2000年第一季度到2017年第一季度批发业对比
x = values[::4, 0]
plt.figure(figsize=(8, 8), dpi=80)

plt.scatter(x, values[::4, 8], marker='o', color='b')

plt.scatter(x, values[::4, 9], marker='o', color='r')
plt.xticks(values[::4, 0], values[::4, 1], rotation=45)
plt.legend(['建筑业', '批发产业'])
plt.show()

