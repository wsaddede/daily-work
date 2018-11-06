import pandas as pd
import numpy as np
movie_data = pd.read_excel('电影分类数据.xlsx')
# print(movie_data)

pos2 = np.array(movie_data.columns[-3:])
# print(pos2)

pos1 = movie_data.loc[:, movie_data.columns[2:5]]

index = np.array(np.sqrt(np.sum((pos1-pos2)**2, axis=1))).argsort()
# print(index)

labels = movie_data.loc[index[:5], '电影类型']

print(labels.mode()[0])
