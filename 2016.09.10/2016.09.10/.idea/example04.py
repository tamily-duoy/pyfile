__author__ = 'v11424'
def vector_add(v, w):
    return [v_i+w_i for v_i, w_i in zip(v, w)]
def vector_subtract(v, w):
    return [v_i-w_i for v_i, w_i in zip(v, w)]

v=[1,2,3,4]
w=[2,3,4,5]
print(vector_add(v, w))
print(vector_subtract(v, w))
