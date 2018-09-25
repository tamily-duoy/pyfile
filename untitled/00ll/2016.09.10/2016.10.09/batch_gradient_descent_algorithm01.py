import numpy as np
import random
import sklearn
from sklearn.datasets.samples_generator import make_regression 
import pylab
from scipy import stats

def gradient_descent(alpha,x,y,ep = .00001, max_iter = 10000):
    converged = False
    iter = 0
    m = x.shape[0]
    t0 = np.random.random(x.shape[1])
    t1 = np.random.random(x.shape[1])
    #print 'this is x shape 1',x.shape[1]
    #now we have  a random hypothesis function h(x) = t0 + t1(x)
    #define J theta
    J = 1.0/(2*m) *sum([(t0 + t1*x[i] - y[i])**2 for i in range(m)])
    while not converged:
        #partial derivatives w/rspt to theta0 and theta1
        d0 = alpha* 1.0/m * sum([(t0 + t1*x[i] - y[i]) for i in range(m)])
        d1 = alpha* 1.0/m * sum([(t0*x[i] + t1*x[i]*x[i] - y[i]*x[i]) for i in range(m)])
        temp0 = t0 - d0
        temp1 = t1 - d1
        #simultaneous update
        t0 = temp0
        t1 = temp1
        print t0,t1
        #recalcuate mean squared error
        newJ = 1.0/(2*m) *sum([(t0 + t1*x[i] - y[i])**2 for i in range(m)])
        if(abs(J - newJ) <= ep):
            converged = True
            print 'Converged, num iterations: ', iter

        J = newJ
        iter = iter + 1

        if(iter == max_iter):
            #finish 
            print 'Max iterations exceeded, ', iter
            converged = True


    return t0,t1


if __name__ == '__main__':

    x, y = make_regression(n_samples=1000, n_features=1, n_informative=1, 
                        random_state=3, noise=999) 
    print 'x.shape = %s y.shape = %s' %(x.shape, y.shape)
 
    alpha = 0.01 # learning rate
    ep = 0.0001 # convergence diff

    theta0, theta1 = gradient_descent(alpha, x, y, ep, max_iter=10000)
    print ('theta0 = %s theta1 = %s') %(theta0, theta1) 

    # check with scipy linear regression 
    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x[:,0], y)
    print ('intercept = %s slope = %s') %(intercept, slope) 

    # plot
    for i in range(x.shape[0]):
        y_predict = theta0 + theta1*x 

    pylab.plot(x,y,'o')
    pylab.plot(x,y_predict,'k-')
    pylab.show()
    print "Done!"
