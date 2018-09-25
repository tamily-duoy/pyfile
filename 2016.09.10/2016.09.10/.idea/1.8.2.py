
#定义导数
def difference_quotient(f,x,h):
    return(f(x+h)-f(x))/h

#定义平方函数
def square(x):
    return x*x
#它的导数为：
def derivative(x):
    return 2*x


x = 4
print(square(x),derivative(x))



#计算一个很小的变动　e的差商　来估算微分
from functools import partial
import numpy as np
def difference_quotient(f,x,h):
	return (f(x+h) - f(x)) / h
def square(x):
	return x * x
def derivative(x):
	return 2 * x
derivative_estimate = partial(difference_quotient, square, h=0.00001)
import matplotlib.pyplot as plt
x = range(-10,10)
plt.title("v")
plt.plot(x,list( map(derivative, x)), 'rx', label = 'Actual')
plt.plot(x, list(map(derivative_estimate, x)), 'b+', label = 'Estimate')
plt.legend(loc=9)
plt.show()

def partial_difference_quotient(f,v,i,h):
	# compute the ith partial difference quotient of f at v
	w = [v_j + (h if j == i else 0)
		 for j, v_j in enumerate(v)]

	return (f(w) - f(v)) / h

def estimate_gradient(f, v, h = 0.00001):
	return [partial_difference_quotient(f,v,i,h)
			for i, _ in enumerate(v)]
