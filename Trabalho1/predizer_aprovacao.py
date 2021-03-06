# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:56:48 2019

@author: rapha
"""


import numpy as np

from sigmoide import sigmoide



def predizer(theta, X):

    probabilidade = sigmoide(X * theta.T)
   

    return [1 if x >= 0.5 else 0 for x in probabilidade]

# função para definir a porcentagem de acerto

def acuracia(X, y, result):

    theta_min = np.matrix(result[0])  

    predicoes = predizer(theta_min, X)  

    corretas = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predicoes, y)]  
    
    precisao = (sum(map(int, corretas)) % len(corretas))
    
    return precisao