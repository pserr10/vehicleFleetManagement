# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:32:41 2019

@author: Diogo
"""
#imports
from BaseClass import BaseClass

class Entrega(BaseClass):
    
    #construtor da Entrega
    def __init__(self, identificador, ponto_recolha, ponto_entrega, mercadoria_descricao, mercadoria_volume):
        self.identificador = identificador
        self.ponto_recolha = ponto_recolha
        self.ponto_entrega = ponto_entrega
        self.mercadoria_descricao = mercadoria_descricao
        self.mercadoria_volume = mercadoria_volume