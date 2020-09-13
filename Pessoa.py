# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:27:55 2019

@author: Diogo
"""
#imports
from BaseClass import BaseClass

class Pessoa(BaseClass):
    
    #construtor da Pessoa
    def __init__(self, numero, nome, telemovel, email):
        self.numero = numero
        self.nome = nome
        self.telemovel = telemovel
        self.email = email