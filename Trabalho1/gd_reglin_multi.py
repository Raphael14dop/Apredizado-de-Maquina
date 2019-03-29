# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:58:49 2019

@author: rapha
"""

import numpy as np

import matplotlib.pyplot as plt

from custo_reglin_multi import custo_reglin_multi


def gd(X, y, alpha, epochs, theta=np.array([0,0,0], ndmin = 2).T):



    m = len(y)



    cost = np.zeros(epochs)

    

    for i in range(epochs):

        h = X.dot(theta)

        loss = h - y

        gradient = X.T.dot(loss) / m

        theta = theta - (alpha * gradient)

        cost[i] = custo_reglin_multi(X, y, theta=theta)
        
        
       
    plt.plot(cost, color='blue',label='Custo')
    plt.title ('Convergência Custo x Iterações')
    plt.xlabel ('Número de Iterações')
    plt.ylabel ('Custo J')
    plt.legend(loc='upper right')
    
       
    filename = 'target/plot2.2.png'
    plt.savefig(filename)    
    
    plt.show()

    #plt.figure(figsize=(12,8))
    
    return cost, theta

