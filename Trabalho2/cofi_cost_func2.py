# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 01:36:14 2019

@author: rapha
"""

import numpy as np





def cofi_cost_func(params, Y, R, num_users, num_movies, num_features, lmd):



    # Obtem as matrizes X e Theta a partir dos params

    X = np.array(params[:num_movies*num_features]).reshape(num_features, num_movies).T.copy()

    Theta = np.array(params[num_movies*num_features:]).reshape(num_features, num_users).T.copy()





    # Voce deve retornar os seguintes valores corretamente

    J = 0

    X_grad = np.zeros(X.shape)

    Theta_grad = np.zeros(Theta.shape)



    # ====================== SEU CODIGO AQUI ======================

    # Instrucoes: calcular a funcao de custo regularizada e gradiente

    # para a filtragem colaborativa. Concretamente, você deve primeiro

    # implementar a funcao de custo. Depois disso, voce deve implementar o

    # gradiente. 

    #

    # Notas: 

    # X - num_movies x num_features: matriz das caracteristicas dos filmes

    # Theta - num_users x num_features: matriz das caracteristicas dos usuarios

    # Y - num_movies x num_users: matriz de classificacoes de filmes por usuarios

    # R - num_movies x num_users: matriz, onde R (i, j) = 1 se o i-esimo filme

    #       foi avaliado pelo j-esimo usuario

    #

    # Voce deve definir as seguintes variaveis ​​corretamente:

    #

    # X_grad - num_movies x num_features matrix, contendo as

    #   derivadas parciais com relacao a cada elemento de X

    # Theta_grad - num_users x num_features: matriz, contendo as

    #   derivadas parciais com relacao a cada elemento de Theta

    # =============================================================
     # compute the cost
     
    error = np.power(np.dot(X,Theta.T) - Y,2)
    #error = np.multiply((X * Theta.T) - Y, R)  # (1682, 943)
    #squared_error = np.power(error, 2)  # (1682, 943)
    #J = (1. / 2) * np.sum(squared_error)
    J = (1/2.)*np.sum(np.multiply(error,R))
    X_grad = np.dot((np.dot(X,Theta.T)- Y)*R,Theta)
    Theta_grad=np.dot(((np.dot(X,Theta.T)-Y)*R).T,X)
    
    # add the cost regularization
    J = J + ((lmd / 2.) * (np.sum(np.power(Theta, 2)) + np.sum(np.power(X, 2))))
   #J = J + ((lmd / 2) * np.sum(np.power(X, 2)))
    
    # calculate the gradients with regularization
    X_grad = X_grad + (lmd * X)
    #X_grad = (error * Theta) + (lmd * X)
    #Theta_grad = (error.T * X) + (lmd * Theta)
    Theta_grad = Theta_grad + (lmd * Theta)
    # unravel the gradient matrices into a single array
   #grad = np.concatenate((np.ravel(X_grad), np.ravel(Theta_grad)))



    grad = np.hstack((X_grad.T.flatten(),Theta_grad.T.flatten()))



    return J, grad