import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

u=np.linspace(-1,1,100)
x,y=np.meshgrid(u,u)
z=x**2+y**2

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

ax.plot_surface(x,y,z,rstride=4,cstride=4,cmap=cm.YlGnBu_r)
plt.show()
