# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:07:18 2019

@author: rapha
"""
import os

import numpy as np

import pandas as pd  

import matplotlib.pyplot as plt

from plot_ex2data2 import importarDados

def executa ():

    data,X,y = importarDados(filepath="\ex2data2.txt", names=['Teste 1', 'Teste 2', 'Aceito'])
    
    X = mapFeature(X[:, 0], X[:, 1])
    print(X)
    
"""
def mapFeature(X1, X2):
    
    #X1 = mat(X1); X2 = mat(X2)

    degree = 6
    out = [np.ones(X1.shape[0])]
    for i in  range(1, degree+1):
        for j in range(0, i+1):
            #out = c_[out, X1.A**(i-j) * X2.A**j] # too slow, what's numpy way?
            out.append(X1**(i-j) * X2**j)
            
            
    return out
    
"""

def mapFeature(x1, x2):

    # potencia dos termos polinomiais das features
    potencia = 6
    #print(x1,x2)
    #tamanho do dataset 
    #map_feature_size = x1.size   
    
    #map_feature = np.ones(shape=(map_feature_size, 1))
    
    map_feature = [np.ones(x1.shape[0])]
    
    #print(map_feature)
    #mapeando as caracteristicas para todos os termos polinomiais de x1 e x2, ate a sexta potencia.
    for i in range(1, potencia + 1):

        for j in range(i + 1):

            #column = (x1 ** (i - j)) * (x2 ** j)

            #map_feature = np.append(map_feature, column, axis=1)

            map_feature.append((x1 ** (i - j)) * (x2 ** j))

    return map_feature
    
 