# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:27:16 2019

@author: Diogo
"""
#imports
from Viatura import Viatura

class Camiao(Viatura):
    _matricula = None
    _capacidade = None
    _exceptionString = "Capacidade tem de ser superior a 1200000 cm3"
    
    #construtor do Camiao
    def __init__(self, matricula, capacidade):
        if self.validate(capacidade) == 1:
            raise Exception(self._exceptionString)
        else: 
            self._matricula = matricula
            self._capacidade = capacidade
    
    #definicao do metodo __str__
    def __str__(self):
        return "{'matricula': " + "'" + str(self.matricula) + "'" + ", 'capacidade': " + str(self.capacidade) + "}"
            
    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        if self.validate(capacidade) == 1:
            raise Exception(self._exceptionString)
        else:
            self._capacidade = capacidade
            
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula
    
    #metodo de validacao das capacidades validas
    def validate(self, capacidade):
        if not (capacidade > 1200000):
            return 1
        else:
            return 0