# -*- coding: utf-8 -*-
"""
Created on Sun May 4 14:10:40 2019

@author: Diogo Soares
"""
#imports
from Automovel import Automovel
from Camiao import Camiao
from Cliente import Cliente
from Condutor import Condutor
from Entrega import Entrega
from Mota import Mota
from queue import Queue
from random import randint, choice
import string
import pickle as pk
from Node import Node

class Programa:
    _nomeApp = "GESTÃO DE FROTA - ESTAFETA"
    _parteProjecto = 2
    #variaveis para inicializacao dos objectos para listas e filas
    _numeroObjectos = 5
    _nomes = ['António', 'Zacarias', 'Francisco', 'Fernando', 'Bruno', 'Joana', 'Maria', 'Isabel', 'Carlota', 'Pedro']
    _tiposViaturas = ['Pesado', 'Ligeiro', 'Motociclo']
    _ponto_recolha = ['Loures', 'Carnide', 'Benfica', 'Lisboa', 'Porto', 'Coimbra', 'Faro']
    _mercadoria_descricao = ['Cadeiras', 'Carne', 'Fruta', 'Pão', 'Material de Construção', 'Computadores', 'Vestuário']
    
    #construtor do Programa
    def __init__(self):
        #listas
        #PT1 - 3.1
        self.listaCamiao = []
        self.listaAutomovel = []
        self.listaMota = []
        self.listaCondutor = []
        self.listaCliente = []
        self.listaEntrega = []
        #filas
        #PT1 - 3.4
        self.FCamiao = Queue()
        self.FAutomovel = Queue()
        self.FMota = Queue()
        self.FCondCamiao = Queue()
        self.FCondAutomovel = Queue()
        self.FCondMota = Queue()
        self.FEntregaCamiao = Queue()
        self.FEntregaAutomovel = Queue()
        self.FEntregaMota = Queue()
        self.cliTree = Node("")
    
    #gera matriculas de veiculos
    #PT1 - 3.2 aux
    def geraMatricula(self, tipo):
        grupo1Letras = str(choice(string.ascii_letters)).upper() + str(choice(string.ascii_letters)).upper()
        grupo2Letras = str(choice(string.ascii_letters)).upper() + str(choice(string.ascii_letters)).upper()
        grupoNumeros = str(randint(0, 9)) + str(randint(0, 9))
        if tipo == 0:
            return grupoNumeros + "-" + grupo1Letras + "-" + grupo2Letras
        if tipo == 1:
            return grupo1Letras + "-" + grupoNumeros + "-" + grupo2Letras
        if tipo == 2:
            return grupo1Letras + "-" + grupo2Letras + "-" + grupoNumeros
    
    #preenche as listas com os seus objectos respectivos
    #PT1 - 3.2
    def preencheListas(self):
        for x in range(self._numeroObjectos):
            self.listaCamiao.append(Camiao(self.geraMatricula(randint(0, 2)), randint(1200000, 1500000)))
            self.listaAutomovel.append(Automovel(self.geraMatricula(randint(0, 2)), randint(80001, 1200000)))
            self.listaMota.append(Mota(self.geraMatricula(randint(0, 2)), randint(0, 80000)))
            nome = choice(self._nomes)
            self.listaCondutor.append(Condutor(x, nome, 91 * 10000000 + randint(0000000, 9999999), nome + "@gmail.com", choice(self._tiposViaturas)))
            self.listaCliente.append(Cliente(x, nome, 91 * 10000000 + randint(0000000, 9999999), nome + "@gmail.com", "Morada" + str(x)))
            self.listaEntrega.append(Entrega(x, choice(self._ponto_recolha), choice(self._ponto_recolha), choice(self._mercadoria_descricao), randint(0, 1500000)))
    
    #metodo para afixar todos os atributos dos objectos que se encontram na lista
    #PT1 - 3.3
    def afixaAtributosObjectosLista(self, listaObjectos):
        for obj in listaObjectos:
            print(obj)
    
    #distribui entregas pelos veiculos
    #PT1 - 3.5
    def distribuiEntregas(self):
        self.FEntregaCamiao.empty()
        self.FEntregaAutomovel.empty()
        self.FEntregaMota.empty()
        for entrega in self.listaEntrega:
          if entrega.mercadoria_volume > 1200000:
              self.FEntregaCamiao.put(entrega)
          elif 80000 < entrega.mercadoria_volume < 1200000:
              self.FEntregaAutomovel.put(entrega)
          elif entrega.mercadoria_volume < 80000:
              self.FEntregaMota.put(entrega)
        
    #preenche as filas com veiculos
    #PT1 - 3.5  
    def preencheFilas(self):
        self.FCamiao.empty()
        self.FAutomovel.empty()
        self.FMota.empty()
        self.FCondCamiao.empty()
        self.FCondAutomovel.empty()
        self.FCondMota.empty()
        for camiao in self.listaCamiao:
            self.FCamiao.put(camiao)
        for automovel in self.listaAutomovel:
            self.FAutomovel.put(automovel)
        for mota in self.listaMota:
            self.FMota.put(mota)
        for condutor in self.listaCondutor:
          if condutor.tipoViatura == "Pesado":
              self.FCondCamiao.put(condutor)
          if condutor.tipoViatura == "Ligeiro":
              self.FCondAutomovel.put(condutor)
          if condutor.tipoViatura == "Motociclo":
              self.FCondMota.put(condutor)
        self.distribuiEntregas()
        
    #metodo que afixa todos os atributos dos objectos de todas as listas
    #aux validador dados PT1
    def afixaTotalListas(self):
        print("\n#Lista Camiões")
        self.afixaAtributosObjectosLista(self.listaCamiao)
        print("\n#Lista Automóveis")
        self.afixaAtributosObjectosLista(self.listaAutomovel)
        print("\n#Lista Motas")
        self.afixaAtributosObjectosLista(self.listaMota)
        print("\n#Lista Condutores")
        self.afixaAtributosObjectosLista(self.listaCondutor)
        print("\n#Lista Clientes")
        self.afixaAtributosObjectosLista(self.listaCliente)
        print("\n#Lista Entregas")
        self.afixaAtributosObjectosLista(self.listaEntrega)
    
    #le e retorna o conteudo do ficheiro Entregas.txt
    def leFicheiroTexto(self):
        self.escreveFicheiroTextoFilas()
        with open('Entregas.txt', 'rt') as f:
            return f.read()
    
    #escreve no ficheiro Entregas.txt
    def escreveFicheiroTexto(self, inputTexto):
        with open('Entregas.txt', 'wt') as f:
            f.write(inputTexto)
    
    #PT2 - 3
    def escreveFicheiroTextoFilas(self):
        auxC = "FEntregaCamiao: \n"
        for c in range(self.FEntregaCamiao.qsize()):
            auxC += str(self.FEntregaCamiao.get().__str__()) + "\n"
        auxA = "FEntregaAutomovel: \n"
        for a in range(self.FEntregaAutomovel.qsize()):
            auxA += str(self.FEntregaAutomovel.get().__str__()) + "\n"
        auxM = "FEntregaMota: \n"
        for m in range(self.FEntregaMota.qsize()):
            auxM += str(self.FEntregaMota.get().__str__()) + "\n"
        self.escreveFicheiroTexto(auxC + "\n" + auxA + "\n" + auxM + "\n")
        self.distribuiEntregas()

    #des-serializa as listas do ficheiro binario EstafetaListas.pickle
    #PT2 - 2
    def leFicheiroBinario(self):
        f = open("EstafetaListas.pickle", "rb")
        self.listaCamiao = pk.load(f)
        self.listaAutomovel = pk.load(f)
        self.listaMota = pk.load(f)
        self.listaCondutor = pk.load(f)
        self.listaCliente = pk.load(f)
        self.listaEntrega = pk.load(f)
        f.close()
        
    #serializa as listas no ficheiro binario EstafetaListas.pickle
    #PT2 - 2
    def escreveFicheiroBinario(self):
        f = open("EstafetaListas.pickle", "wb")
        pk.dump(self.listaCamiao, f)
        pk.dump(self.listaAutomovel, f)
        pk.dump(self.listaMota, f)
        pk.dump(self.listaCondutor, f)
        pk.dump(self.listaCliente, f)
        pk.dump(self.listaEntrega, f)
        f.close()
    
    #adiciona veiculo à lista respectiva
    #PT2 - 2
    def adicionaVeiculo(self):
            matricula = input("Matrícula: ")
            capacidade = int(input("Capacidade: "))
            if capacidade > 1200000:
                self.listaCamiao.append(Camiao(matricula, capacidade))
            elif 80000 < capacidade < 1200000:
                self.listaAutomovel.append(Automovel(matricula, capacidade))
            elif capacidade < 80000:
                self.listaMota.append(Mota(matricula, capacidade))
    
    #adiciona condutor à lista respectiva
    def adicionaCondutor(self):
        identificador = int(input("Identificador: "))
        nome = input("Nome: ")
        numero = int(input("Número: "))
        email = input("E-mail: ")
        tipoViatura = input("Tipo de Viatura (" + ", ". join(self._tiposViaturas) + "): ")
        self.listaCondutor.append(Condutor(identificador, nome, numero, email, tipoViatura))
    
    #adiciona cliente à lista respectiva
    def adicionaCliente(self):
        identificador = int(input("Identificador: "))
        nome = input("Nome: ")
        numero = int(input("Número: "))
        email = input("E-mail: ")
        morada = input("Morada: ")
        self.listaCliente.append(Cliente(identificador, nome, numero, email, morada))
    
    #adiciona entrega à lista respectiva
    def adicionaEntrega(self):
        identificador = int(input("Identificador: "))
        pontoRecolha = input("Ponto de Recolha: ")
        pontoEntrega = input("Ponto de Entrega: ")
        mercadoriaDescricao = input("Descrição da mercadoria: ")
        mercadoriaVolume = int(input("Volume da mercadoria: "))
        self.listaEntrega.append(Entrega(identificador, pontoRecolha, pontoEntrega, mercadoriaDescricao, mercadoriaVolume))
        
    def insereNomesClientesTree(self):
        if len(self.listaCliente) > 0:
            for c in self.listaCliente:
                self.cliTree.binary_insert(self.cliTree, Node(c.nome)) 
                
    def afixaNomesClientesTreeOrdem(self):
        self.cliTree.in_order_print(self.cliTree)
    
    def existeNomeTree(self):
        nomeCliente = str(input("Introduza o nome do cliente: "))
        if self.cliTree.findvalue(self.cliTree, nomeCliente):
            print("Existe o nome " + nomeCliente + " na árvore.")
        else:
            print("Não existe o nome " + nomeCliente + " na árvore.")

    #imprime o menu
    def printMenu(self):
        print("----------------- Menu -----------------")
        print("1 - Adicionar Veículo")
        print("2 - Adicionar Condutor")
        print("3 - Adicionar Cliente")
        print("4 - Adicionar Entrega")
        print("5 - Afixar Listas")
        print("6 - Preencher Filas")
        print("7 - Ler ficheiro de texto")
        print("8 - Ler ficheiro binário")
        print("9 - Escrever ficheiro binário")
        print("10 - Inserir nomes da ListaCliente na árvore")
        print("11 - Verificar se existe Cliente na árvore")
        print("12 - Afixar nomes dos clientes contidos na árvore ordenados crescentemente")
        print("13 - Sair da aplicação")
                
    #funcao de controlo de escolha no menu
    def control(self):
        choice = input("Escolha uma das opções apresentadas:\n")
        if choice == "1":
            print("--------------- Adicionar Veículo --------------")
            self.adicionaVeiculo()
        elif choice == "2":
            print("-------------- Adicionar Condutor ---------------")
            self.adicionaCondutor()
        elif choice == "3":
            print("-------------- Adicionar Cliente ---------------")
            self.adicionaCliente()
        elif choice == "4":
            print("-------------- Adicionar Entrega ---------------")
            self.adicionaEntrega()
        elif choice == "5":
            print("---------------- Afixar Listas -----------------")
            self.afixaTotalListas()
        elif choice == "6":
            print("--------------- Preencher Filas ----------------")
            self.preencheFilas()
        elif choice == "7":
            print("------------- Ler ficheiro de texto ------------")
            try:
                print(self.leFicheiroTexto())
            except:
                print("O ficheiro não existe.")
        elif choice == "8":
            print("- Ler ficheiro binário -")
            try:
                print(self.leFicheiroBinario())
                print("Sucesso!\n")
            except:
                print("O ficheiro não existe.")
                #self.preencheListas()
                #self.escreveFicheiroBinario()
                #print(self.leFicheiroBinario())
        elif choice == "9":
            print("- Escrever ficheiro binário -")
            try:
                print(self.escreveFicheiroBinario())
                print("Sucesso!\n")
            except:
                print("Surgiu um erro ao escrever o ficheiro binário.")
        elif choice == "10":
            print("- Inserir nomes da ListaCliente na árvore -")
            self.insereNomesClientesTree()
            print("Sucesso!\n")
        elif choice == "11":
            print("- Verificar se existe Cliente na árvore -")
            self.existeNomeTree()
        elif choice == "12":
            print("- Afixar nomes dos clientes contidos na árvore ordenados crescentemente -")
            self.afixaNomesClientesTreeOrdem()
        elif choice == "13":
            try:
                self.escreveFicheiroBinario()
            except:
                pass
            print("Obrigado por ter utilizado a aplicação " + self._nomeApp + "\n" + "Adeus! :D")
            return 0
        else:
            print("Não existe a opção " + choice + ". Por favor selecionar opções de 1 a 5")
    
    def initControl(self):
        while 1:
            choice = input("Deseja utilizar Listas de Dados:\n1) já existentes\n2) com novos dados a introduzir.\n")
            if int(choice) == 1:
                try:
                    self.leFicheiroBinario()
                    print("Ficheiro binário lido com sucesso.")
                except:
                    print("O ficheiro não existe.")
                    self.preencheListas()
                    self.escreveFicheiroBinario()
                    print(self.leFicheiroBinario())
                break
            elif int(choice) == 2:
                try:
                    self.escreveFicheiroBinario()
                except:
                    pass
                break
            else:
                print("Não existe a opção " + choice + ". Por favor selecionar opções 1 ou 2")
    
    def main(self):
        print("##############  " + self._nomeApp + "  ##############")
        #metodo principal PT1
        def mainPT1():
            self.preencheListas()
            self.preencheFilas()  
            self.afixaTotalListas()
        #metodo principal PT2
        def mainPT2():
            self.initControl()
            while True:
                self.printMenu()
                if self.control() == 0:
                    break
        if self._parteProjecto == 1:
            mainPT1()
        else:
            mainPT2()


programaEstafeta = Programa()
programaEstafeta.main()
