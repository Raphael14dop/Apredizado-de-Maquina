# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:52:43 2019

@author: rapha
"""

import numpy as np





def sigmoide(z):

    return 1.0 / (1 + np.exp(-z))