# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:41:06 2019

@author: rapha
"""


import numpy as np

from sigmoide import sigmoide
from gd_reglog import gd_reglog

    
   
    
def funcaoCustoRegressaoLogistica(theta,X,y):

    theta = np.matrix(theta)

    X = np.matrix(X)

    y = np.matrix(y)

    grad0 = np.multiply(-y, np.log(sigmoide(X * theta.T)))

    grad1 = np.multiply((1 - y), np.log(1 - sigmoide(X * theta.T)))

    return np.sum(grad0 - grad1) / (len(X))

