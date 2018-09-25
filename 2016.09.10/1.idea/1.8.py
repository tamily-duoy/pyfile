# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 19:47:34 2016

@author: Administrator
"""

def square(x):
    return x*x
#def sum_of_squares(v):
  #  """computes the sumof squared elements in v"""
   # return sum(v_i for v_i in v)
def difference_quotient(f,x,h):
    return (f(x+h)-f(x))/h
def derivative(x):
    return 2*x
from functools import partial
derivative_estimate=partial(difference_quotient,square,h=0.00001)


def partial_difference_quotient(f,v,i,h):
    """compute the ith partial difference quotient of f at v"""
    w=[v_j + (h if j==i else 0)  #
       for j,v_j in enumerate(v)]
    return(f(w)-f(v))/h
def estimate_gradient(f,v,h=0.00001):
    return[partial_difference_quotient(f,v,i,h)
            for i,_ in enumerate(v)]

x=range(-10,10)
import matplotlib.pyplot as plt
plt.title("v")
plt.plot(x,map(derivative,x),'rx',label="a")
plt.plot(x,map(derivative_estimate,x),'b+',label="b")
plt.show()




def step(v,direction,step_size):
    """move step_size in the direction from v"""
    return[v_i + step_size*direction_i
           for v_i,direction_i in zip(v,direction)]


#1.8.5
def safe(f):
    """return a new function that is the same as f, except that it outputs 
    infinity whenever f produces an error"""
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')             # this means "inifinity" in Python
    
    return safe_f

def step(v,direction,step_size):
    """move step_size in the direction from v"""
    return[v_i + step_size*direction_i
           for v_i,direction_i in zip(v,direction)]




def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """use gradient descent to find theta that minimizes the target function"""
    
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    
    theta = theta_0                 # set theta to initial value
    target_fn = safe(target_fn)     # safe version of target_fn
    value = target_fn(theta)        # value we are minimizing
    
    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size) 
                       for step_size in step_sizes]
        
        # choose the one that maximizes the error function
        next_theta = min(next_thetas, key=target_fn)
        next_value= target_fn(next_theta)
        
        # stop if we are "converging"
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value
            
"""
Sometimes, we'll instead want to maximize a function, which we can do by minimizing 
its negative
"""
def negate(f):
    """return a function that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
    """negation for when f returns a list of numbers"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn),
                          negate_all(gradient_fn),
                          theta_0,
                          tolerance)
