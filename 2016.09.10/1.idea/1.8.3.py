import random
import math
from random import randint


v = [1,1]
w = [1,2]
def vector_subtract(v,w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]
def dot(v, w):
    return sum(v_i*w_i for v_i, w_i in zip(v, w))
def sum_of_squares(v):
    return dot(v,v)
def squared_distance(v, w):
#(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2
    return sum_of_squares(vector_subtract(v, w))
def distance(v, w):
    return math.sqrt(squared_distance(v, w))


def step(v,direction,step_size):
    """move step_size in the derection from v"""
    return [v_i + step_size *direction_i
            for v_i,direction_i in zip(v,direction)]
def sum_of_squares_gradient(v):
    return[2*v_i for v_i in v]

v =[random.randint(-10,10) for i in range(3)]
tolerance=0.0000001
while True:
    gradient=sum_of_squares_gradient(v)
    next_v = step(v,gradient,-0.01)
    if distance(next_v,v)<tolerance:
        break
    v = next_v