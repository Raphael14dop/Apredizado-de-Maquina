# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:33:42 2019

@author: rapha
"""

import os

import numpy as np

import pandas as pd  

import matplotlib.pyplot as plt


def executa ():

    data,X,y = importarDados(filepath="\ex2data2.txt", names=['Teste 1', 'Teste 2', 'Aceito'])
    
    #print(data)
    plot(data)

def importarDados(filepath,names):

    path = os.getcwd() + filepath

    data = pd.read_csv(path,delimiter=",", header=None, names=names)

    insertOnes=True

    # Carregando os dados do dataset e armazendo em um array. Em seguida damos uma rapida visualizada nos dados

    data.head()



    # A primeira coluna, preenchida com 1's, represenhta o theta0

   
    #if insertOnes:

       #data.insert(0, 'Ones', 1)
 


    # converte de dataframes para arrays

    cols = data.shape[1]

    X = data.iloc[:, 0:cols - 1]

    y = data.iloc[:, cols - 1:cols]



    # converte de arrays para matrizes

    X = np.array(X.values)

    y = np.array(y.values)



    return data,X, y



def plot(data):



    # gerando o grafico de dispersao para analise preliminar dos dados



    Aceito = data[data['Aceito'].isin([1])]

    Rejeitado = data[data['Aceito'].isin([0])]



    fig, ax = plt.subplots(figsize=(12,8))

    ax.scatter(Aceito['Teste 1'], Aceito['Teste 2'], s=50, c='k', marker='+', label='y=1')

    ax.scatter(Rejeitado['Teste 1'], Rejeitado['Teste 2'], s=50, c='y', marker='o', label='y=0')

    ax.legend()

    ax.set_xlabel('Microchip Teste 1')

    ax.set_ylabel('Microchip Teste 2')


    filename = 'target/plot4.1.png'

    if not os.path.exists(os.path.dirname(filename)):

        os.makedirs(os.path.dirname(filename))



    plt.savefig(filename)

    plt.show()