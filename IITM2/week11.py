##### PANDAS #####

# f = open('IITM2/scores.csv', 'r')
# scores = f.readlines()[1:]
# max = 0
# for record in scores:
#     fields = record.split(',')
#     if int(fields[8]) > max:
#         max  = int(fields[8])
# print(max)

import pandas as pd
scores = pd.read_csv("IITM2/scores.csv")
# print(scores["total"].max())
# print(scores["total"].min())
# print(scores["total"].mean())
# print(scores["total"].sum())
# print(scores.describe())
# print(scores.head)
# print(scores.head(n=5))
# print(scores.tail)
# print(scores.tail(n=1))
# print(scores.count)

# print(scores.sort_values("total"))
# print(scores.sort_values("total", ascending=False))
# print(scores[scores["gender"] == "M"]["total"].max())
# print([scores["gender"] == "M"])
# print(scores["physic"].between(70,75, inclusive='right'))
# print(scores.groupby("gender").groups)
# print(len(scores.groupby("gender").groups["F"]))
# print(scores.dtypes)


##### NUMPY #####
# import numpy as np
# a = [1]
# b = [1,2]
# c = [[1,2], [3,4]]


##### Filtering #####
# x_zero  = np.zeros((2,3))
# print(x_zero)

# range_x = np.arange(5)
# print(range_x)

# print(np.linspace(0,1,5))
# print(range_x[1:3])


##### MatplotLib #####

import numpy as np
import matplotlib.pyplot as plt
# x  = np.array([5,7,8,7,2,17,2,9,4,11])
# y = np.array([99,86,87,88,111,86,103,87,94,78])
# plt.scatter(x,y)
# plt.title("scatter plot")
# plt.show()


# x = ["A", "B", "C", "D"]
# y = [3,8,1,10]
# plt.bar(x,y)
# plt.title("Bar Graph")
# plt.show()

# plt.barh(x,y)
# plt.title("Bar Graph")
# plt.show()

# data = np.random.normal(150, 10, 250)
# plt.hist(data)
# plt.title("Histogram")
# plt.show()

# plt.pie(y, labels=x)
# plt.title("pie chart")
# plt.show()

x = np.arange(0, 10, 0.1)
plt.figure(figsize=(10, 6))

plt.subplot(2,3,1)
plt.plot(x, x)
plt.title('y = x')

plt.subplot(2, 3, 1)
plt.plot(x, x**2)
plt.title('y = x^2')

plt.subplot(2, 3, 3)
plt.plot(x, np.sqrt(x))
plt.plot("y = sqrt(x)")

plt.subplot(2, 3, 4)
plt.plot(x, np.sin(x))
plt.title("y = sin(x)")

plt.subplot(2, 3, 5)
plt.plot(x, np.cos(x))
plt.title("y = cos(x)")

plt.subplot(2,3,6)
plt.plot(x, -x)
plt.title("x = -x")

plt.show()