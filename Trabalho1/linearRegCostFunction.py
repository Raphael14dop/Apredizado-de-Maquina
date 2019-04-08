# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 00:29:42 2019

@author: rapha
"""


import numpy as np

from scipy.optimize import minimize

# Função para otimizar o valor de theta

def linearRegCostFunction(X, y, lmd):
    
    theta_inicial = np.array([[15],[15]]) 
    res = minimize(RegCostFunction, theta_inicial, args=(X,y,lmd), method=None, jac=gradientReg, options={'maxiter':5000})
       
    return(res)
    
    #Função para o calculo do custo
def RegCostFunction(theta, X, y, lmd):

    m = len(y)

    h = X.dot(theta)

    J = (1/(2*m))*np.sum(np.square(h-y)) + (lmd/(2*m))*np.sum(np.square(theta[1:]))

    return(J)
    
    # Função para o calculo do gradiente
    
def gradientReg(theta, X, y, lmd):

    m = len(y)

    h = X.dot(theta.reshape(-1,1))
    
    grad = (1/m)*(X.T.dot(h-y))+ (lmd/m)*np.r_[[[0]],theta[1:].reshape(-1,1)]

    return(grad.flatten())
    
    
