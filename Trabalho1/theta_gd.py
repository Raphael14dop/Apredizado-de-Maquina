# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 00:56:15 2019

@author: rapha
"""

import numpy as np

from gd_reglin_uni import gd_reglin_uni
from custo_reglin_uni import custo_regrlin

    
def theta_gd(theta):
    
    # São criados dois Arrays para o calculo da populaçao referente a 70.000 e 35.000. 
    
    x7 = np.array([1, 7])
    x35 = np.array([1, 3.5])
    
    # São armazenados os valores multiplicado por theta passado como parâmetro 
    
    theta_gd70 = (x7.dot(theta)).reshape(-1,1)[0,0]
    theta_gd35 = (x35.dot(theta)).reshape(-1,1)[0,0]
    print ("Lucro em regiões com populações de 35.000 habitantes = $ %.2f" % (10000.0*theta_gd35))
    print ("Lucro em regiões com populações de 70.000 habitantes = $ %.2f" % (10000.0*theta_gd70))
    

    