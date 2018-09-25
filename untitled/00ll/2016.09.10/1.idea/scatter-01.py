import matplotlib.pyplot as plt

plt.xlim(xmax=7,xmin=0)   #设置边界
plt.ylim(ymax=7,ymin=0)

plt.annotate("(3,6)",xy=(3,6),xytext=(4,5),
             arrowprops=dict(facecolor='yellow',shrink=0.1))
#设置标注
plt.plot([1,2,3],[4,5,6],'ro')#　'ro'　去掉后变成直线，贯穿点的直线
plt.title("diagram  scatter")
plt.show()