class Elemento:
    def _init_(self, valor, proximo=None, anterior=None):
        self.valor = valor
        self.proximo = proximo
        self.anterior = anterior

class ListaDupla:
    def _init_(self):
        self.primeiro = None

    # Fábrica de criar novos elementos:
    def criarNovoElemento(self, valorQualquer):
        e = Elemento(valorQualquer, None, None)  # valor, proximo, anterior
        return e

    def imprimeLista(self):
        aux = self.primeiro
        if aux is not None:
            while aux is not None:
                print(aux.valor)
                aux = aux.proximo
        else:
            print("--- Lista Vazia ---")

    def addElementoNoFinal(self, valorQualquer):
        novo = self.criarNovoElemento(valorQualquer)
        if self.primeiro is None:
            self.primeiro = novo
        else:
            aux = self.primeiro
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = novo
            novo.anterior = aux  # Liga o novo nó ao último elemento

    def removeElementoNoFinal(self):
        if self.primeiro is None:
            print("--- Lista Vazia ---")
            return

        if self.primeiro.proximo is None:
            del(self.primeiro)
            self.primeiro = None
            print("--- Lista Vazia novamente ---")
            return

        aux = self.primeiro
        while aux.proximo is not None:
            aux = aux.proximo
        aux.anterior.proximo = None
        del(aux)

    def addElementoNoInicio(self, valorQualquer):
        novo = self.criarNovoElemento(valorQualquer)
        if self.primeiro is None:
            self.primeiro = novo
        else:
            novo.proximo = self.primeiro
            self.primeiro.anterior = novo
            self.primeiro = novo

    def removeElementoNoInicio(self):
        if self.primeiro is None:
            print("--- Lista Vazia ---")
            return

        if self.primeiro.proximo is None:
            del(self.primeiro)
            self.primeiro = None
        else:
            aux = self.primeiro
            self.primeiro = self.primeiro.proximo
            self.primeiro.anterior = None
            del(aux)

    def removeQualquerElemento(self, v):
        if self.primeiro is None:
            print("--- Lista Vazia ---")
            return

        aux = self.primeiro
        while aux is not None:
            if aux.valor == v:
                if aux == self.primeiro:
                    self.removeElementoNoInicio()
                elif aux.proximo is None:
                    self.removeElementoNoFinal()
                else:
                    aux.anterior.proximo = aux.proximo
                    aux.proximo.anterior = aux.anterior
                    del(aux)
                return
            aux = aux.proximo

        print("--- Valor não encontrado ---")


# MAIN
# Criando uma lista VAZIA
minhaLista = ListaDupla()
minhaLista.addElementoNoFinal(91)
minhaLista.addElementoNoFinal(92)
minhaLista.addElementoNoFinal(93)
minhaLista.addElementoNoFinal(94)

minhaLista.imprimeLista()
print("---------------------")

minhaLista.removeQualquerElemento(100)  # Tentando remover um valor que não existe
minhaLista.imprimeLista()