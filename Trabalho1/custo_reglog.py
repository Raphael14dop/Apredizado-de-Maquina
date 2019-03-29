# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:41:06 2019

@author: rapha
"""


import numpy as np

from sigmoide import sigmoide
from gd_reglog import gd_reglog

    
    # Funçao alterada para Retornar o valor do custo e gradiente
    
def custo_reglog(theta, X, y):

    theta = np.matrix(theta)

    X = np.matrix(X)

    y = np.matrix(y)

    grad0 = np.multiply(-y, np.log(sigmoide(X * theta.T)))

    grad1 = np.multiply((1 - y), np.log(1 - sigmoide(X * theta.T)))
    
    # Funçao Retorna o valor do custo e gradiente
    
    resultado = np.sum(grad0 - grad1) / (len(X))
    
    grad = gd_reglog(theta,X,y)

    return resultado,grad