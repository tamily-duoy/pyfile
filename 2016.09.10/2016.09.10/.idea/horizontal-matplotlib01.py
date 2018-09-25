import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

label = ['a','b','c','d','e','f']
x = sorted([1234,221,765,124,2312,890])

idx = np.arange(len(x))
color = cm.jet(np.array(x)/max(x))
plt.barh(idx, x, color = color)
plt.yticks(idx+0.4,label)
plt.grid(axis='x')

plt.xlabel('Revenues Earned')
plt.ylabel('Salespeople')
plt.title('Top 12 Salespeople(2012)\n(in USD)')

plt.show()