# 剔除餐饮菜品中整列为空或者取值完全相等的列
import pandas as pd

detail = pd.read_excel('./meal_order_detail.xlsx')

# detail.drop(labels='', axis=1, inplace=True)
# print(detail[:].describe())
# print(detail.shape[1])

# data = detail[:].describe()
# print(data)
# for i in data:
#     print(i)




# 1.全为空值  2.全为相同值
# count/        unique/max=min/freq=count/var=0/std=0

# colisnull = detail.describe().loc['count'] == 0
# print(colisnull)

# for i in range(len(colisnull)):
#     if colisnull[i]:
#         detail.drop(colisnull.index[i], axis=1, inplace=True)
# print(detail.shape[1])

# stdiszero = detail.describe().loc['std'] == 0

# 删除相同值
# for j in range(len(stdiszero)):
#     if stdiszero[j]:
#         detail.drop(stdiszero.index[j], axis=1, inplace=True)
# print(detail.shape[1])

