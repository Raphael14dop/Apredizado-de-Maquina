# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 00:39:34 2019

@author: rapha
"""

import numpy as np

from sigmoide import sigmoide

def costFunctionReg(theta, X, y, lmd):

    m = len(y)
    
    h_theta = sigmoide(X * [theta])
    J = -1./m * (y.T.dot(np.log(h_theta)) + (1-y).T.dot(np.log(1 - h_theta)))
    J_reg = lmd/(2*m) * (theta[1:] ** 2).sum()
    J = J_reg +J

       
    return J[0][0]