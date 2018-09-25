# -*- coding: utf-8 -*-




"""
In the general case, we have a "target function" that we want to minimize,
and we also have its "gradient function". Also, we have chosen a starting
value for the parameters "theta_0".
"""







#例子１

import matplotlib.pyplot as plt

movies = ["Annie Hall", "Ben-Hur","Cassblanca" , "Candhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
xs = [i + 0.1 for i,_ in enumerate(movies)]  #条形图的默认宽度是０．８　，因此在左侧坐标加上０．１　　　＃这样，每个条形就被放在中心
plt.bar(xs, num_oscars)#使用左侧x坐标【xs】和高度【num_oscars】画条形图
plt.ylabel("v")      #所获得奥斯卡金像奖数量
plt.title("m")     #我最喜爱的电影
plt.xticks([i + 0.5 for i,_ in enumerate(movies)], movies)#使用电影的名字标记x轴，位置在x轴上条形的中心
plt.show()


#修改版
import numpy as np
import matplotlib.pyplot as plt

movies = ["Annie Hall", "Ben-Hur","Cassblanca" , "Candhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
xs = np.arange(len(movies))  #条形图的默认宽度是０．８　，因此在左侧坐标加上０．１　　　＃这样，每个条形就被放在中心
#使用左侧x坐标【xs】和高度【num_oscars】画条形图
plt.ylabel("v")         #所获得奥斯卡金像奖数量
plt.title("m")         #电影名字
plt.xticks(xs+0.4,movies)#使用电影的名字标记x轴，位置在x轴上条形的中心
plt.bar(xs, num_oscars)
plt.show()



#例子２
import  matplotlib.pyplot as plt
import numpy as np
from collections import Counter
#条形图也可以绘制拥有大量数值取值的变量直方图，以此来探索这些取值如何分布

x = [83,95,91,87,70,0,85,82,100,67,73,77,0]
y = lambda grade:grade//10*10
z = Counter(y(i) for i in x)

#print(z)得到以下
#Counter({80: 4, 70: 3, 0: 2, 90: 2, 100: 1, 60: 1})


plt.bar([j - 4 for j in z.keys()],        #每个条形图向左移动４个单位
        z.values(),                     #给每个条形设置正确的高度
        8)#每个条形宽度设置为８　
plt.axis([-5, 105, 0, 5])                        # x轴取值为－５到１０５　　　　＃y轴取值为０到５
plt.xticks([10 * i for i in range(11)])           #轴标记为０，　１０，　．．．１００
#plt.xlabel("十分相")
#plt.ylabel("学生数")
plt.title(["考试分数分布图"])
plt.show()




#例子３

#如此巨大的增长
mentions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel("听到有人提及‘数据科学’的次数")#如果不这么做，matplotlib会把x轴的刻度标记为０和１　　＃然后会在角上加上＋２．０１３e3(糟糕的matplotlib操作)
plt.ticklabel_format(useOffset = False)
#这会误导y轴只显示５００以上的部分
plt.axis([2012.5, 2014.5, 499, 506])
plt.title("快看如此’巨大’的增长")
plt.show()

#增长不那么
plt.axis([2012.5, 2014.5, 0, 550])
plt.title("增长不那么巨大了")
plt.show()

