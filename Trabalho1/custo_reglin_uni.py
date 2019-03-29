# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:40:06 2019

@author: rapha
"""

import numpy as np
from plot_ex1data1 import importarDados


def custo_regrlin(X, y, theta):
    
    """"
    "Após implementar essa função, você pode verificar a cor-
retude executando com todos os parâmetros iguais a zero. Nessa situação, sua
função deve gerar um valor igual a 32,07."
"""
    # Quantidade de exemplos de treinamento
    m = len(y)
        # Computar a funcao do custo J
    J = (np.sum((X.dot(theta) - y)**2)) / (2 * m)
    
    return J