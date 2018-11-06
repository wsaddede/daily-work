
import pandas as pd

detail=pd.read_excel(r'C:\Users\Administrator\Desktop\meal_order_detail.xlsx')
print(detail.shape)
detail = detail.dropna(axis=1)
# print(detail.describe())
# print(detail.shape)
detail = detail.ix[:, (detail != detail.ix[0]).any()]
# print(detail.ix[0])
# print(detail != detail.ix[0])