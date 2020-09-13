# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:24:04 2019

@author: Diogo
"""
#imports
from BaseClass import BaseClass

class Viatura(BaseClass):
    
    #construtor da Viatura
    def __init__(self, matricula, capacidade):
        self.matricula = matricula
        self.capacidade = capacidade