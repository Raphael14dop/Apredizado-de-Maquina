# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:43:54 2019

@author: rapha
"""
import os
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from custo_reglin_uni import custo_regrlin

from plot_ex1data1 import importarDados


def executa ():

    data = importarDados(filepath="\ex1data1.txt", names=["Population","Profit"])
    custo, theta = gd_reglin_uni(data.X,data.y, 0.01, 5000)
    print(custo)

def gd_reglin_uni(X, y, alpha, epochs, theta = np.array([0,0], ndmin = 2).T):


    m = len(y)

    cost = np.zeros(epochs)

    for i in range(epochs):

        h = X.dot(theta)
        loss = h - y
        gradient = X.T.dot(loss) / m
        theta = theta - (alpha * gradient)
        cost[i] = custo_regrlin(X, y, theta = theta)
        

    
   # plt.figure(figsize=(12,8))
    #plt.plot(cost, color='blue')
    #plt.title ('Convergência Custo x Iterações')
    #plt.xlabel ('Iterações')
    #plt.ylabel ('Custo')
    #plt.legend()
    #plt.show()
    filename = 'target/plot1.3.png'

    if not os.path.exists(os.path.dirname(filename)):

        os.makedirs(os.path.dirname(filename))
        

    return cost[-1], theta