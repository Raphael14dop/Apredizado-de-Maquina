# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 01:14:55 2019

@author: rapha
"""

import numpy as np

from linearRegCostFunction import linearRegCostFunction

from linearRegCostFunction import regCostFunction

""" Utilizando a função Para learningCurve para traçaar a 
curva de aprendizado,e definindo um conjunto de treinamento e validação 
cruzada erro para diferentes tamanhos de conjuntos de treinamento.
"""

def learningCurve(X, y, Xval, yval, lmd):

    m = y.size

    erro_treino = np.zeros((m, 1))

    erro_val = np.zeros((m, 1))

    for i in np.arange(m):
        
        # Otimizando o valor de theta

        res = linearRegCostFunction(X[:i+1], y[:i+1], lmd)
        
        # Defindo um conjunto de erro de treinamento 

        erro_treino[i] = regCostFunction(res.x, X[:i+1], y[:i+1], lmd)
        
         # Defindo erro de validação cruzada

        erro_val[i] = regCostFunction(res.x, Xval, yval, lmd)

    

    return(erro_treino, erro_val)