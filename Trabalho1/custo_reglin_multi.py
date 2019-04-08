# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:43:57 2019

@author: rapha
"""

import numpy as np

def custo_reglin_multi(X, y, theta):

    # Quantidade de exemplos

    m = len(X)



    # Computa a funcao de custo J

    J = (np.sum((X.dot(theta)- y)**2))/ (2 * m)



    return J