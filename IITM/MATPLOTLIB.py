import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x, y)
plt.show()

categories = np.array(["a", "b", "c", "d"])
values = np.array([3, 8, 1, 10])
plt.barh(categories, values)
plt.bar(categories, values)
plt.show()

samples = np.random.normal(170, 10, 250)
plt.hist(samples)
plt.show()

counts = np.array([35, 25, 15])
labels = ["apple", "banana", "cherries"]
plt.pie(counts, labels=labels, startangle=90)
plt.show()
