# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:40:06 2019

@author: rapha
"""

import numpy as np
from plot_ex1data1 import importarDados


def executa ():

    data = importarDados(filepath="\ex1data1.txt", names=["Population","Profit"])
    #custo, theta = gd_reglin_uni(data.X,data.y, 0.01, 7000)
    #print(custo,theta)
    theta = np.array([0,0]).reshape(-1, 1)
    result = (custo_regrlin(data.X,data.y,theta))
    print (result)

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