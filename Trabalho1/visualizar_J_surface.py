# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 01:31:53 2019

@author: rapha
"""

import os

import numpy as np

import matplotlib.pyplot as plt

from custo_reglin_uni import custo_regrlin
#Usado para plotar 3d em fig.gca

#from mpl_toolkits.mplot3d import Axes3D


def plot(data):

    # Valores de theta0 e theta1 informados no enunciado do trabalho

    theta0 = np.arange(-10, 10, 0.01)

    theta1 = np.arange(-1, 4, 0.01)



    # Comandos necessarios para o matplotlib plotar em 3D

    fig = plt.figure()

    ax = fig.gca(projection='3d')
    
    J = np.zeros((len(theta0), len(theta1)))

    for i in range(len(theta0)):

        for j in range(len(theta1)):

            t = [[theta0[i]], [theta1[j]]]
            
            J[i,j] = custo_regrlin(data.X, data.y, t)
    
    # Plotando o grafico de superficie
    J = np.transpose(J)
      
    theta0, theta1 = np.meshgrid(theta0, theta1)
    
    surf = ax.plot_surface(theta0, theta1, J,rstride=3, cstride=3, cmap=plt.cm.jet, linewidth=0.3, antialiased=True)

    plt.xlabel('theta_0')

    plt.ylabel('theta_1')

    plt.title(r'Função de custo $J(\theta)$')
    
    



    filename = 'target/plot1.3.2.png'

    if not os.path.exists(os.path.dirname(filename)):

        os.makedirs(os.path.dirname(filename))



    plt.savefig(filename)

    plt.show()

    return surf