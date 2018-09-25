#-*- encoding:utf-8 -*-


from sklearn import datasets
iris=datasets.load_iris()

#data对应了样本的4个特征，150行4列
# print iris.data.shape
#
# #显示样本特征的前5行
# print iris.data[:5]
#
# #target对应了样本的类别（目标属性），150行1列
# print iris.target.shape
#
# #显示所有样本的目标属性
# print iris.target

def load_dataset(dataset,len_x,len_y):
    dataset=open(dataset,'r')
    line=dataset.readline()
    X=list()
    Y=list()
    while line:
        l=line.strip('\n')
        l=l.split(' ')
        l = [ float( l ) for l in l if l ]
        X.append(l[0:len_x])
        Y.append(l[len_x:len_x+len_y])
        line=dataset.readline()
    return (X,Y)
print


















































import numpy as np

# def file2matrix(filename):
#     myfile = open(filename)
#     arrayOLines=myfile.readlines()
#     numberOfLines=len(arrayOLines)    #按行读
#
#     returnMat=zeros((numberOfLines,4))   #创建m行3列的零矩阵
#     classLabelVector = []
#     index = 0
#     print returnMat
#     ##解析数据到列表
#     for line in arrayOLines:
#         line = line.strip()        #删除行前面的空格(截取掉所有的回车字符)
#         listFormLine = line.split('\t')    #根据分隔符划分(使用tab字符\t将上步得到的整行数据分割成一个元素列表)
#
#         returnMat [index,:] = listFormLine[0:3]   #每一行的内容存起来(特征矩阵中)
#         classLabelVector.append(int(listFormLine[-1])) #Python语言可以使用索引值-1表示列表中最后一个元素，很方便的将列表最后一列存储到向量classLabelVector中）
#         index += 1
#      return returnMat,classLabelVector
#
# datingDataMat,DatingLabels = file2matrix(r'C:\Users\Administrator\.spyder\00ll\2016.09.10\simple_matplotloib\IrisData.txt','r')
#
#
# def test():
#     b = 'test string'
#
# if __name__ =='__main__':
#     test()
#
#
#
#
#
#
#













# list_arr = myfile.readlines()
#
#
#
#
#
#
#
#
#
#
#
#
# l = len(list_arr)
# for i in range(l):
#     list_arr[i] = list_arr[i].strip()
#     list_arr[i] = list_arr[i].strip('[]')
#     # list_arr[i] = list_arr[i].split(", ")
# a = np.array(list_arr)
# # a = a.astype(int)
# a = list_arr
#
# print a[0] ,type(a)
# # myfile.close()
#









# myfile = open(r'C:\Users\Administrator\.spyder\00ll\2016.09.10\simple_matplotloib\IrisData.txt','r')
# datasets = myfile.read()
# result = []
# for line in datasets.readlines():
#     result.append(list(map(int,line.split(','))))
# print(result)


# datasetsL=list(datasets)

# def splist(l,s):
#     return [l[i:i+s] for i in range(len(l)) if i%s==0]
#
# b = splist(datasetsL,5)
#
# print datasetsL[0]








# list = ['5.1,3.5,1.4,0.2,Iri-ssetosa']
# print list[3]