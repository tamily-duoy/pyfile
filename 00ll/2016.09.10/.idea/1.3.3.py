import matplotlib.pyplot as plt
#import numpy as np
variance     = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error  = [x+y for x,y in zip(variance,bias_squared)]
xs = [i for i,_ in enumerate(variance)]#类似于xs = np.arange(len(variance))

plt.plot(xs,variance,'g-',label='variance')
plt.plot(xs,bias_squared,'r-.',label = 'bias^2')
plt.plot(xs,total_error,'b:',label='total error')
plt.legend(loc=9)      #将图例设置在图的“顶部中央”
plt.xlabel("v")
plt.title("m")
plt.show()
