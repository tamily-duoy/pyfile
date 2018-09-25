height_weight_age=[70,  #英寸
                   170, #磅
                   40]  #岁

grades = [95,  #考试一
          80,  #考试二
          75,  #考试三
          62]  #考试四



#定义两向量相加 相减
def vector_add(v,m):
    """adds corresponding elements"""
    return [v_i + w_i for v_i,w_i in zip(v,w)]
def vector_suntract(v,m):
    """subtracts corresponding elements"""
    return [v_i - w_i for v_i,w_i in zip(v,m)]

v=[1,2]
w=[2,3]
print(vector_add(v,w))
print(vector_suntract(v,w))



#定义多个向量的相加

def vector_add(v,m):
    """adds corresponding elements"""
    return [v_i + w_i for v_i,w_i in zip(v,w)]

def vector_sum(vectors):
    """sums all corresponding elements"""
    result=vectors[0]
    for vector in vectors[1:]:
        result=vector_add(result,vector)
        return result
v=[1,2]
w=[2,3]
vectors=(v,w)
print(vector_sum(vectors))