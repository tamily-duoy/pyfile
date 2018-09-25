import numpy as np
import matplotlib.pyplot as plt
x = [0,1,2,4,5,6]
y = [1,2,3,2,4,1]
z = [1,2,3,4,5,6]
plt.figure(1)
plt.subplot(211)
plt.plot(x,y,'-+b')
plt.subplot(212)
plt.plot(x,z,'-.*r')
plt.show()
