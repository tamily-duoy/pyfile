import  numpy as np
import matplotlib.pyplot as plt
line1, = plt.plot([1,2,3])
line2, = plt.plot([3,2,1],'--b')
plt.legend((line1,line2),('line1','line2'))
plt.show()