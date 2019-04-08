# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 01:55:43 2019

@author: rapha
"""
import numpy as np

from sigmoide import sigmoide

def gradientReg(theta, X, y, lmd):
    
    m = len(y)
    
    grad = (1/m)*X.T.dot(sigmoide(X.dot(theta.reshape(-1,1)))-y) + (lmd/m)*np.r_[[[0]],theta[1:].reshape(-1,1)]
     
    
    return grad.flatten()