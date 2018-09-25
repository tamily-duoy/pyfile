import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

x = np.array([0.46,0.59,0.68,0.99,0.39,0.31,1.09,0.77,0.72,0.49,0.55,0.62,0.58,0.88,0.78]) # x is a numpy array now
y = np.array([0.315,0.383,0.452,0.650,0.279,0.215,0.727,0.512,0.478,0.335,0.365,0.424,0.390,0.585,0.511]) # y is a numpy array now
xerr = [0.01]*15
yerr = [0.001]*15

plt.rc('font', family='serif', size=13)
m, b = np.polyfit(x, y, 1)
plt.plot(x,y,'s',color='#0066FF')
plt.plot(x, m*x + b, 'r-') #BREAKS ON THIS LINE
plt.errorbar(x,y,xerr=xerr,yerr=0,linestyle="None",color='black')
plt.xlabel('$\Delta t$ $(s)$',fontsize=20)
plt.ylabel('$\Delta p$ $(hPa)$',fontsize=20)
plt.autoscale(enable=True, axis=u'both', tight=False)
plt.grid(False)
plt.xlim(0.2,1.2)
plt.ylim(0,0.8)
plt.show()
