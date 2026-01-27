import numpy as np
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a, a.ndim, '\n')
print(b, b.ndim, '\n')
print(c, c.ndim, '\n')
print(d, d.ndim, '\n')


# f = open('score.csv','r')
# scores = f.readlines()[1:]
# max = 0
# for record in scores:
#     fields = record.split(',')
#     if int(fields[8]) > max:
#         max = int(fields[8])
# print(max)


# import pandas as pd
# score = pd.read_csv('score.csv')
# print(score)
# print(score.shape)
# print(score.count)
# print(score[' Total'].mean())
# print(score[' Total'].sum())
# print(score[' Total'].sort_values())


import pandas as pd
score = pd.read_csv('score.csv')
print(score.columns)
# print(score.groupby(' Gender').groups)
print(score[score[' chem']>85])
print(score[score[' physics'].between(70,85)])
print(score[score[' physics'].between(60,70)])
