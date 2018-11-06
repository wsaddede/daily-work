# pandas
import pandas as pd

##csv:是一种应用分隔符分隔的文件，因为其分隔符不一定是逗号————又称为字符分隔文件；
##文件以纯文本形式存储表格数据(数字和文本)
##：csv文件是文本的一种特殊形式，可以读取txt/csv读取方式读取

###csv读取文件方法
order=pd.read_csv(r'C:\Users\Administrator\Desktop\meal_order_info.csv',sep=',',encoding='gbk')


# print(order)
##文本文件读取方法，参数：1、路径,2、分隔符，3，编码方式
# pd.read_table()
###注意：sep参数是指定文本分隔符，如果读取的时候指定错了，读取的数据将连成一片；

##
# pd.to_csv('文件名称.csv',sep=';',index=False)
##index代表是否将行名（索引）写出，默认为True,
##columns=[列表]  #表示列名

#####Excel文件读取与存储：#################
#扩展名：
# .xls 2007年之前的版本/
# .xlsx 2007年之后的版本

detail=pd.read_excel(r'C:\Users\Administrator\Desktop\meal_order_detail.xlsx')
# print(detail)




##存储文件：
# user.to_excel('文件名.xls')

#######DataFrame 的常用操作：
# DataFrame 的常用属性：
# values/columns/dtypes/
# print(user.values)##所有值
# print(user.columns)##列表名
# print(user.dtypes)##数据类型
# print(user.shape)
# print(user.size)
# print(user.ndim)
##转置
# print(order.T.shape)
# print(order.shape)
# print(order.index)

####查改增删DataFrame数据：
#获取'dishes_name','order_id'这两列数据的前5个值
# print(detail[['dishes_name','order_id']][:5])
#获取所有列的2:5行
# print(detail[:][1:6])

##head/tail函数：获取前5行/后5行数据：()中可以传想读的行数或列数
# print(detail.head())
# print(detail.tail(6))

####loc/iloc函数
# loc函数针对索引名称的切片，如果传入的不是索引名称，那么将无法切片；
# iloc函数传入的是索引；
# loc[行索引名称或条件，列索引名称]
# iloc[行索引位置，列索引位置]

###单列切片：
# print(detail.loc[:,'dishes_name'])
# print(detail.iloc[:,2])

##多列切片：
# print(detail.loc[:,['order_id','dishes_name']].size)
# print(detail.iloc[:,[2,5]])

# print(detail.loc[3,['order_id','dishes_name']])
# print(detail.iloc[3,[2,5]])

# 条件切片：
# print(detail.loc[detail['order_id']==458,['order_id','dishes_name']])
# print(detail.iloc[(detail['order_id']==458).values,[1,5]])


###更改dataframe:
##将order__id=458的值更改为45800
# detail.loc[detail['order_id']==458,'order_id']=45800
# print(detail.loc[detail['order_id']==45800,['order_id','dishes_name']])
#
# ##填数据
# detail['payment']=detail['counts']*detail['amounts']
# # print(detail['payment'])
# detail['payway']='现金支付'
# # print(detail['payment'])
#
# ##drop删除：
# # inplace:是否对原表生效；默认为False
# # labels:删除的行或者列的标签
# detail.drop(labels='payway',axis=1,inplace=True)
# # print(detail.columns)
# print(len(detail))
# detail.drop(labels=range(1,11),axis=0,inplace=True)
# print(len(detail))

###numpy 统计分析函数：10个
##中位数：median
##众数：mode
##非空数目：count

##describe第一种用法：
# print(detail[['counts','amounts']].describe())

# 返回：返回非空列数，均值，最小，最大，标准差，四分位数（8个值）
##describe第二种用法：将数据类型转换为category,再配合describe使用：
# detail['dishes_name']=detail['dishes_name'].astype('category')
# print(type(detail['dishes_name']))
# print(detail['dishes_name'].dtypes)
# print(detail['dishes_name'].describe())

##返回非空列数，类别数目，数目最多的类别，数目最多的类别数（四个）

####剔除餐饮菜品中整列为空或者取值完全相等的列：














