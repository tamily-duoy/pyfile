def best(w,w1,traindataIn,trainlabelIn):
    trainData=mat(traindataIn)
    trainlabel=mat(trainlabelIn)
    num=0
    num1=0
    m,n=shape(trainData)
    for i in range(m):
        if(sigmoid(dot(trainData[i],w))!=trainlabel[i]):
            num=num+1
        if(sigmoid(dot(trainData[i],w1))!=trainlabel[i]):
            num1=num1+1
        i=i+1
    if num<num1:#w作为最后的结果错误比较少
        return w
    else:
        return w1
#测试集合
def classifyall(datatest,w):
    predict=[]
    for data in datatest:
        result=classify(data,w)
        predict.append(result)
    return predict