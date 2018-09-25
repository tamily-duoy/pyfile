  # encoding:utf-8
from numpy import *
import sklearn
import sklearn.datasets
import matplotlib.pyplot as plt
import matplotlib
import operator
import sklearn.linear_model
import time
import matplotlib

random.seed(0)
X, y = sklearn.datasets.make_moons(200, noise=0.2)  # 创造二分类的数据集
plt.scatter(X[:, 0], X[:, 1], s=40, c=y,
            cmap=plt.cm.Spectral)  # cmap里面的参数为一种布局方式，y在此处既代表点的种类，也代表点的颜色，http://matplotlib.org/api/colors_api.html
clf = sklearn.linear_model.LogisticRegressionCV()
clf.fit(X, y)

# Plot the decision boundary
plt.title("Logistic Regression")
plt.show()