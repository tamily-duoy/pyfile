# -*- coding:utf-8 -*-
import numpy
import rbm
import sys
import time

class DBN:
    def __init__(self, net=[], k=5):
        self.k=k
        self.net=net
        self.layers=len(net)
        self.W=[]
        self.hbias=[]
        self.dbn_rbm=[]
        for i in range(self.layers-1):
            numpy_rng = numpy.random.RandomState(123+i)
            a=1./net[i]
            self.dbn_rbm.append(rbm.RBM(input=None, n_visible=net[i], n_hidden=net[i+1], W=None, hbias=None,
                                   vbias=None, numpy_rng=None))
            W , hbias =self.dbn_rbm[i].get_parameter()
            self.W.append(W)
            self.hbias.append(hbias)

    def get_parameter(self):
        for i in range(self.layers-1):
            self.W.append(self.dbn_rbm[0].get_parameter())
        return self.W

    def get_data(self, filename, k=5):
        data=[]
        userids=[]
        itemids=[]
        rates=[]
        for line in open(filename):
            linestr=line.split()
            lineint=[int (linestr[i]) for i in range(len(linestr))]
            ratevec=[0 for i in range(k)]
            ratevec[lineint[2]-1]=1
            lineint[2]=ratevec
            userids.append(lineint[0])
            itemids.append(lineint[1])
            rates.append(lineint[2])
        self.userids=userids
        self.itemids=itemids
        self.rates=rates
        return userids,itemids,rates

    def train(self):
        self.first_hidden_value=numpy.zeros((len(self.rates),self.net[1]))
        for i in range(len(self.rates)):
            #print "processing rating: " ,i
            Wsel=self.W[0][self.itemids[i]:self.itemids[i]+self.k]

            #print Wsel
            self.first_rbm=rbm.RBM(numpy.array([self.rates[i]]), n_visible=self.k, n_hidden=self.net[1],
                                 W=Wsel, hbias=None, vbias=None, numpy_rng=None)

            self.first_rbm.contrastive_divergence(lr=0.001, k=5)

            after_W, afterhbias = self.first_rbm.get_parameter()
            self.W[0][self.itemids[i]:self.itemids[i]+self.k] = after_W
            #self.first_hidden_value[i]=self.first_rbm.get_hidden_value()

if __name__=="__main__":
    start_time=time.time()
    #print time.strftime('%H:%M:%S',time.localtime(time.time()))
    dbn=DBN([3847*5,100,2,3847*5],5)
    userids,itemids,rates=dbn.get_data("shratings.dat",5)
    dbn.train()
    end_time=time.time()
    print time.strftime('%H:%M:%S',time.localtime(end_time-start_time))

