import pandas as pd
import numpy as np
order = pd.read_csv('./meal_order_info.csv', sep=',', encoding='gbk')
order['locks_time'] = pd.to_datetime(order['lock_time'])
order['user_start_time'] = pd.to_datetime(order['use_start_time'])

# 每个用户下单所用时间
# time_end = order['locks_time'] - order['user_start_time']
# print(time_end)
# for i in time_end:
#     print(i)

# 最早,最晚下单时间  以及差值
order['day1']=[i.day for i in order['user_start_time']]

group_time1=order[['day1','user_start_time']].groupby(by='day1')

day_time=group_time1['user_start_time'].max()-group_time1['user_start_time'].min()
print('差值',day_time)
#餐厅每天平均营业时间
order['day1']=[i.day for i in order['user_start_time']]
order['day2']=[i.day for i in order['lock_time']]

group_time1=order[['day1','user_start_time']].groupby(by='day1')
group_time2=order[['day2','lock_time']].groupby(by='day2')

time=group_time2['lock_time'].max()-group_time1['user_start_time'].min()
print('平均营业时间：',time)
