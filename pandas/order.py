import pandas as pd
order = pd.read_csv(r'C:\Users\Administrator\Desktop\meal_order_info.csv',encoding='gbk')
# print(order.head())
detail_info = pd.read_excel(r'C:\Users\Administrator\Desktop\meal_order_detail.xlsx')

user1 = pd.read_excel(r'C:\Users\Administrator\Desktop\users.xlsx')

columns = list(detail_info.columns)
# print(columns)
print(detail_info.shape)
for i in columns:
    act = detail_info[i].astype('category')
    # print(act.describe())
    if (not act.describe().loc['count']) or (act.describe().loc['unique'] ==1):
        detail_info.drop(labels = i,axis = 1,inplace = True)
print(detail_info[detail_info.columns])