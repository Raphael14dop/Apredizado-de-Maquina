# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:43:54 2019

@author: rapha
"""
import os
import numpy as np

import matplotlib.pyplot as plt

from custo_reglin_uni import custo_regrlin

"""
Função para o calculo do gradiente, passando como parâmetro a variavel grafico. Onde caso
 seja True é gerado grafico de convergência.

"""

def gd_reglin_uni(X, y, alpha, epochs,grafico, theta = np.array([0,0],ndmin = 2).T):


    m = len(y)

    cost = np.zeros(epochs)
    
    #Realizando calculo do custo

    for i in range(epochs):

        h = X.dot(theta)
        loss = h - y
        gradient = X.T.dot(loss) / m
        theta = theta - (alpha * gradient)
        cost[i] = custo_regrlin(X, y, theta = theta)
        
        #Condição para Plotar gráfico de convergência Custo x Iterações 

    if (grafico == True):
        
        plt.figure(figsize=(12,8))
        plt.plot(cost, color='blue')
        plt.title ('Convergência Custo x Iterações')
        plt.xlabel ('Iterações')
        plt.ylabel ('Custo')
        plt.legend()
        filename = 'target/plot1.3.0.png'
        if not os.path.exists(os.path.dirname(filename)):

            os.makedirs(os.path.dirname(filename))
        plt.savefig(filename)
        plt.show()

    return cost[-1], theta