# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:31:00 2019

@author: Diogo
"""
#imports
from Pessoa import Pessoa

class Condutor(Pessoa):
    
    #construtor do Condutor
    def __init__(self, numero, nome, telemovel, email, tipoViatura):
        super().__init__(numero, nome, telemovel, email)
        self.tipoViatura = tipoViatura