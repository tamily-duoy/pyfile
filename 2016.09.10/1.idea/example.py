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