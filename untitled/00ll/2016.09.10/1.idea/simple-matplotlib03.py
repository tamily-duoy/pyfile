# -*- coding: utf-8 -*-
#!/usr/bin/env python     #多线图
import numpy as np
import matplotlib.pyplot as plt
x = [0,1,2,4,5,6]
y = [1,2,3,2,4,1]
z = [1,2,3,4,5,6]
plt.plot(x,y,'--*r',x,z,'-.+g')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("hello world")
plt.show()
