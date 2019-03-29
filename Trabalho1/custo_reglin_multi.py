# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 00:00:59 2019

@author: rapha
"""

import numpy as np





def custo_reglin_multi(X, y, theta):

    # Quantidade de exemplos
    #m = np.array.shape[0]
    m = len(y)
    
   


    # Computa a funcao de custo J

    J = (np.sum((X.dot(theta)- y)**2))/ (2 * m)



    return J