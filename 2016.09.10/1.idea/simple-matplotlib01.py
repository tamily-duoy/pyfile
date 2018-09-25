import matplotlib.pyplot as plt   #导入pyplot子库
plt.figure(figsize=(8, 4))  #创建一个绘图对象, 并设置对象的宽度和高度, 如果不创建直接调用plot, Matplotlib会直接创建一个绘图对象
plt.plot([1, 2, 3, 4])  #此处设置y的坐标为[1, 2, 3, 4], 则x的坐标默认为[0, 1, 2, 3]在绘图对象中进行绘图, 可以设置label, color和linewidth关键字参数
plt.ylabel('some numbers')  #给y轴添加标签, 给x轴加标签用xlable
plt.title("hello");  #给2D图加标题
plt.show()  #显示2D图p



x = [0,1,2,3,]
y = [1,2,3,4,]
plt.plot(x,y,'-')#此处设置y的坐标为[1, 2, 3, 4], 则x的坐标默认为[0, 1, 2, 3]在绘图对象中进行绘图, 可以设置label, color和linewidth关键字参数
等价于
plt.plot([1, 2, 3, 4])