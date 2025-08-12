from app import Elemento

class Circular:
    def __init__(self):
        self.primeiro = None
    def criarNovoElemento(self, valor):
        e = Elemento(valor)
        return e
        
    def adicionarNoFim(self, valor):
        novo = self.criarNovoElemento(valor)
        if self.primeiro is None:
            self.primeiro = novo
        else:
            aux = self.primeiro
            while (aux.proximo != None):
                aux = aux.proximo
            aux.proximo = novo
            
    def adicionarNoInicio(self, valor):
        novo = self.criarNovoElemento(valor)
        if (self.primeiro == None):
            self.primeiro = novo
        else:
            novo.proximo = self.primeiro
            self.primeiro = novo
            
    def adicionarNaPosicao(self, valor, posicao):
        novo = self.criarNovoElemento(valor)
        if posicao < 0:
            print("Posição inválida")
            return
        if posicao == 0:
            self.adicionarNoInicio(valor)
            return
        aux = self.primeiro
        for i in range(posicao - 1):
            if (aux == None):
                print("Posição fora do alcance da lista")
                return
            aux = aux.proximo
        if (aux == None):
            print("Posição fora do alcance da lista")
        else:
            novo.proximo = aux.proximo
            aux.proximo = novo
            
    def removerDoInicio(self):
        if (self.primeiro == None):
            print("Lista vazia")
            return
        self.primeiro = self.primeiro.proximo
        
    def removerDoFim(self):
        if (self.primeiro == None):
            print("Lista vazia")
            return
        if (self.primeiro.proximo == None):
            self.primeiro = None
            return
        aux = self.primeiro
        while (aux.proximo.proximo != None):
            aux = aux.proximo
        aux.proximo = None
        
    def removerDaPosicao(self, posicao):
        if (self.primeiro == None):
            print("Lista vazia")
            return
        if posicao < 0:
            print("Posição inválida")
            return
        if posicao == 1:
            self.removerDoInicio()
            return
        aux = self.primeiro
        for i in range(posicao - 2):
            if (aux.proximo == None):
                print("Posição fora do alcance da lista")
                return
            aux = aux.proximo
        if (aux.proximo == None):
            print("Posição fora do alcance da lista")
        else:
            aux.proximo = aux.proximo.proximo
            
    def imprimirLista(self):
        if self.primeiro is None:
            print("Lista vazia")
        else:
            aux = self.primeiro
            while aux is not None:
                print(aux.valor, end=" -> ")
                aux = aux.proximo
            print("None")

    def contarElementos(self):
        if self.primeiro is None:
            return 0
        contador = 0
        aux = self.primeiro
        while (aux != None):
            contador += 1
            aux = aux.proximo
        return contador