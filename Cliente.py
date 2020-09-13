# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:32:04 2019

@author: Diogo
"""
#imports
from Pessoa import Pessoa

class Cliente(Pessoa):
    
    #construtor do Cliente
    def __init__(self, numero, nome, telemovel, email, morada):
        super().__init__(numero, nome, telemovel, email)
        self.morada = morada