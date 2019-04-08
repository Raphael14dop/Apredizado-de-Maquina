# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 01:24:55 2019

@author: rapha
"""

def polyFeatures(X, p):

    """

    Nesta parte sera implementado codigo em um arquivo de nome polyFeatures.py.

    Uma funcao mapeia o conjunto de treinamento original X

    de tamanho m X 1 em suas potencias mais altas.

    Especificamente, quando um conjunto de treinamento X

    de tamanho mX 1 for passado para essa funcao, ela

    deve retornar uma matriz m X p de nome X.poli, onde a coluna 1 contem

    os valores originais de x,

    a coluna 2 contem os valores de x^2, a coluna 3 contem

    os valores de x^3, e assim por diante.

    

    Parametros

    ----------

    X : ndarray, shape (n_samples, 1)

        Atributos a serem mapeados

    p : int

        Potencia dos atributos polinomiais.



    Returns

    -------

    ndarray, shape (n_samples, p)

        Polynomial features.

    """

    X_poly = X

    if p >= 2:

        for k in range(1,p):

            X_poly = np.column_stack((X_poly, np.power(X,k+1)))

    return X_poly