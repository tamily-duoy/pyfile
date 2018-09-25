# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import numpy as np
import idx2numpy
import image
import struct
import pickle

# images = idx2numpy.convert_from_file("train-images.idx3-ubyte")
#-------------------------------------------------------------------------------
#---------------------------数据------------------------------------------------
# 训练集文件
train_images_idx3_ubyte_file = 'C:/Users/Administrator/.spyder/00ll/2017/train-images.idx3-ubyte'

# 测试集文件
test_images_idx3_ubyte_file = 'C:/Users/Administrator/.spyder/00ll/2017/t10k-images.idx3-ubyte'


def decode_idx3_ubyte(idx3_ubyte_file):
    """
    解析idx3文件的通用函数
    :param idx3_ubyte_file: idx3文件路径
    :return: 数据集
    """
    # 以二进制读模式打开数据    .read（）会读取文件的所有内容
    bin_data = open(idx3_ubyte_file, 'rb').read()

    # 解析文件头信息，依次为魔数、图片数量、每张图片高、每张图片宽
    offset = 0   #将光标移到offset定义的下标位置,在此处开始插入或读取文件
    fmt_header = '>iiii'   # header函数是解析报头的函数
    magic_number, num_images, num_rows, num_cols = struct.unpack_from(fmt_header, bin_data, offset)
    print '魔数:%d, 图片数量: %d张, 图片大小: %d*%d' % (magic_number, num_images, num_rows, num_cols)

    # 解析数据集
    image_size = num_rows * num_cols
    offset += struct.calcsize(fmt_header)
    fmt_image = '>' + str(image_size) + 'B'
    images = np.empty((num_images, num_rows, num_cols))
    for i in range(num_images):
        if (i + 1) % 10000 == 0:
            print '已解析 %d' % (i + 1) + '张'
        images[i] = np.array(struct.unpack_from(fmt_image, bin_data, offset)).reshape((num_rows, num_cols))
        offset += struct.calcsize(fmt_image)
    return images

# Reading
images = decode_idx3_ubyte('train-images.idx3-ubyte')

f_read = open('train-images.idx3-ubyte', 'rb')
# images = idx2numpy.convert_from_file(f_read)
#images = f_read.read()
# s = f_read.read()
# images = idx2numpy.convert_from_string(s)

data = []
temp = []

for image in images:
    for i in image:
        for j in i:
            temp.append(float(j))
    data.append(temp)
    temp = []
X = np.asarray(data, 'float32')
# X = np.asarray(data, 'string')
X = X / 255.0
Y = idx2numpy.convert_from_file("train-labels.idx1-ubyte")
X_test = X[50000:]
Y_test = Y[50000:]
X = X[:50000]
Y = Y[:50000]

sizes = [X.shape[1], 100]


class rbm:
    def __init__(self, sizes=[], learning_rate=0.01, numepochs=1):
        print 'rbm init ,sizes:', sizes, ', numepochs:', numepochs
        self.W = np.matrix(np.zeros(sizes, 'float32'))
        self.vW = np.matrix(np.zeros(sizes, 'float32'))

        self.b = np.matrix(np.zeros(sizes[0], 'float32'))
        self.vb = np.matrix(np.zeros(sizes[0], 'float32'))

        self.c = np.matrix(np.zeros(sizes[1], 'float32'))
        self.vc = np.matrix(np.zeros(sizes[1], 'float32'))

        self.learning_rate = learning_rate
        self.numepochs = numepochs

        self.v1 = self.b
        self.v2 = self.b
        self.h1 = self.c
        self.h2 = self.c
        self.c1 = self.W
        self.c2 = self.W

    def sigmrnd(self, X):
        return np.float32(1. / (1. + np.exp(-X)) > np.random.random(X.shape))

    def train(self, X):
        print 'begin train , X.shape', X.shape, 'numepochs:', self.numepochs
        for i in range(self.numepochs):
            err = 0
            for v in X:
                self.v1 = np.matrix(v)

                self.h1 = self.sigmrnd(self.c + np.dot(self.v1, self.W))
                self.v2 = self.sigmrnd(self.b + np.dot(self.h1, self.W.T))
                self.h2 = self.sigmrnd(self.c + np.dot(self.v2, self.W))

                self.c1 = np.dot(self.h1.T, self.v1).T
                self.c2 = np.dot(self.h2.T, self.v2).T

                self.vW = self.learning_rate * (self.c1 - self.c2)
                self.vb = self.learning_rate * (self.v1 - self.v2)
                self.vc = self.learning_rate * (self.h1 - self.h2)

                self.W = self.W + self.vW
                self.b = self.b + self.vb
                self.c = self.c + self.vc

                err = err + np.linalg.norm(self.v1 - self.v2)
            print "err :", err
        return self.W, self.b, self.c

    def predict(self, X):
        m, n = X.shape
        return self.sigmrnd(np.dot(np.ones((m, 1)), self.c) + np.dot(X, self.W))


class dbn:
    def __init__(self, sizes=[], learning_rate=0.01, numepochs=1):

        print 'dbn init ,sizes:', sizes, ', numepochs:', numepochs
        self.sizes = sizes
        self.rbms = []
        self.learning_rate = learning_rate
        self.numepochs = numepochs
        self.X = []

        for i in range(len(self.sizes) - 1):
            self.rbms.append(rbm(sizes[i:i + 2], 0.01, self.numepochs))

    def train(self, X):
        self.X.append(X)
        # for i in range(self.numepochs):
        for j in range(len(self.sizes) - 1):
            self.rbms[j].train(self.X[j])
            self.X.append(self.rbms[j].predict(self.X[j]))

    def predict(self, X):
        for j in range(len(self.sizes) - 1):
            X = self.rbms[j].predict(X)
        return X


sizes = [X.shape[1], 200, 100]
dbn1 = dbn(sizes, 0.01, 4)
dbn1.train(X)


def sigmoid(X):
    return 1.0 / (1.0 + np.exp(-X))


def gradAscent(data, labels, label):
    m, n = data.shape
    alpha = 0.01
    weights = np.ones((n, 1))
    # numepochs = 1

    # for k in range(numepochs):
    #    h=sigmoid(data*weights)
    #    err = (labels-h)
    #    weights = weights + alpha*data.T*err
    print 'gradAscent begin'
    numiter = 1
    for j in range(numiter):
        print "numiter:", j
        dataIndex = range(m)
        for i in range(m):
            alpha = 4.0 / (1.0 + j + i) + 0.01
            randIndex = int(np.random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(data[randIndex] * weights))
            err = float(labels[randIndex] == label) - h
            weights = weights + alpha * (data[randIndex].T) * err
            del (dataIndex[randIndex])
    return weights


# weights = gradAscent(rbm1.predict(X),Y,7)
weights = []
for i in range(10):
    weights.append(gradAscent(dbn1.predict(X), Y, i))




def test():
    sum1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sum2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    index = 0
    for i in dbn1.predict(X_test):
        temppre = -1000
        tempY = -1000
        for j in range(10):
            pre = i * weights[j]
            if pre > temppre:
                temppre = pre
                tempY = j
        if tempY == Y_test[index]:
            sum1[Y_test[index]] = sum1[Y_test[index]] + 1
        sum2[Y_test[index]] = sum2[Y_test[index]] + 1
        index = index + 1
    for i in range(10):
        print float(sum1[i]) / float(sum2[i]), ' , ', sum1[i], '/', sum2[i]


test()

im = image.open('3.bmp')
t = np.array(im)
tt = []
for i in t:
    for j in i:
        tt.append(j)
target = []
target.append(tt)
target = np.asarray(target, 'float32')
target = target / 255.0  # 0-1 scaling

temppre = -100
tempY = -100

for j in range(10):
    pre = dbn1.predict(target) * weights[j]
    if pre > temppre:
        temppre = pre
        tempY = j
print tempY


