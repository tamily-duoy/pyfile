# -*- coding: utf-8 -*-




"""
In the general case, we have a "target function" that we want to minimize,
and we also have its "gradient function". Also, we have chosen a starting
value for the parameters "theta_0".
"""


import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt                              #导入模块
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]    #导入数据
plt.plot(years, gdp, color = 'green', marker = 'o', linestyle = 'solid') #图
plt.title("gdp")#添加标题
plt.ylabel("m")
plt.show()

