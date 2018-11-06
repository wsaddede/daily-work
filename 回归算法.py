from sklearn.datasets import load_boston
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 加载数据
boston = load_boston()

# data：数据   target：标签  特征名称：feature_name
# 描述信息：DESCR

# 取标签：以字典的形式进行取值
y = boston['target']
# 取特征名称
names = boston['feature_names']
# 获取数据集数据
X = boston['data']

# 导入到.xls文件中
# 创建文件名称及其路径
# outputfile = r'boston.xls'
# # 将数据表和标签表两张表合并为一整个数据大表
# df = pd.DataFrame(X, index=range(len(y)), columns=names)
# pf = pd.DataFrame(y, index=range(len(y)), columns=['outcome'])
# j = df.join(pf, how='outer')
# # 将数据表存入文件中
# j.to_excel(outputfile)

# 第一步 ：分割样本
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 第二步 构造线性回归模型
clf = LinearRegression().fit(X_train, y_train)

# 查看模型
print('截距', clf.intercept_)
print('回归系数：', clf.coef_)
# 预测训练集结果
y_predict = clf.predict(X_test)

fig = plt.figure(figsize=(10, 6))
rcParams['font.sans-serif'] = 'SimHei'



plt.plot(range(y_test.shape[0]), y_test, color='blue', linewidth=1.0, linestyle='-')
plt.plot(range(y_predict.shape[0]), y_predict, color='red', linewidth=1.0, linestyle='-.')

plt.legend(['真实房价', '预测房价'])
plt.savefig('回归结果.png')
plt.show()

# 模型评价标准
# 绝对偏差
# 方差：真实值：var  预测值var
#  mean((y_predict-y_text) ^2)

