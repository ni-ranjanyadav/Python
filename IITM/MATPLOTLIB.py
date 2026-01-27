import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()

x = np.array(['a', 'b', 'c', 'd'])
y = np.array([3,8,1,10])
plt.barh(x, y)
plt.bar(x, y)
plt.show()

x = np.random.normal(170,10,250)
plt.hist(x)
plt.show()

y = np.array([35, 25, 15])
mylabels = ['apple', 'banana', 'cherrries', 'dates']
plt.pie(y,labels = mylabels, startangle = 90)
plt.show()

