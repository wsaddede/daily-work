import matplotlib.pyplot as plt
import numpy as np

# 基本绘图流程
# 1、确定xy的值
# x = np.linspace(-1, 1, 20)
#
# # y=2x+1
# y = 2 * x + 1
# # print(y)
# y2 = x**2

# 2.画图
# 第一步 创建空白画布
# plt.figure()
#
# # 第二步画图 传xy
#
# plt.plot(x, y, color='red', linewidth=2.0, linestyle='-.', marker='v', markersize=5, markerFaceColor='g')
# plt.plot(x, y2)
#
# # 解决中文不显示问题
# plt.rcParams['font.sans-serif'] = 'SimHei'
# # 解决保存图片是负号‘-’ 显示为方块的问题
# plt.rcParams['axes.unicode_minus'] = False
# # 添加图标题
# plt.title('直线')
# # 添加坐标轴名称
# plt.xlabel('x轴')
# plt.ylabel('y轴')
# # x.y轴范围
# plt.xlim((-0.5, 0.5))
# plt.ylim((0, 2))
# # xy的刻度
# plt.xticks([-1, 0, 1])
# plt.yticks([-1, 1, 3])
# # 图例
# plt.legend(['y=2x+1', 'y=x^2'])

# 边框设置
# ax = plt.gca()  # 获取轴的信息
# ax.spines['right'].set_color('none')  # 取消右边边框
# ax.spines['top'].set_color('none')  # 取消上边边框


# 第三步 显示图片
# plt.show()
#######################################################
# 1、确定xy的值
pi = np.pi

# x = np.linspace(0, 2*pi, 50)
x = np.arange(0, pi*2, 0.1)
# y=2x+1

y2 = x**2
y3 = np.sin(x)
y4 = np.cos(x)
# r1 = np.sqrt(pi**2 - x**2)

# 第一步 创建空白画布
p1 = plt.figure(figsize=(8, 8), dpi=80)
# 第二步 添加子图
p1.add_subplot(2, 2, 1)
plt.plot(y3, y4, color='red', mec='b', markersize=20, marker='*')
plt.legend([' '])

p1.add_subplot(2, 2, 2)
plt.plot(x, y2, color='blue')
plt.legend(['y=x^2'])

p1.add_subplot(2, 2, 3)
plt.plot(x, y3, color='y')
plt.legend(['y3 = np.sin(x)'])

p1.add_subplot(2, 2, 4)
plt.plot(x, y4, color='g')
plt.legend(['y4 = np.cos(x)'])

# 先保存 后显示
# plt.savefig('绘图1.png')

plt.show()


