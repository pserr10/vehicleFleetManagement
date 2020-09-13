# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:25:15 2019

@author: Diogo
"""

class BaseClass:
    
    #construtor nao valido para a BaseClass
    def __init__(self):
        raise Exception('Not today.')
    
    #definicao do metodo __str__ que ira ser utilizado para todas as classes que herdarem de BaseClass
    def __str__(self):
        return str(vars(self))