class Elemento:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo    
class Lista:
    def __init__(self):
        self.primeiro = None

    # Fábrica de criar novos elementos:
    def criarNovoElemento(self, valorQualquer):
        e = Elemento(valorQualquer, None)
        return e

    def imprimeLista(self):
        aux = self.primeiro
        if aux is not None:
            while aux is not None:    
                print(aux.valor)
                aux = aux.prouximo
        else:
            print("--- Lista Vazia ---")

    def addElementoNoFinal(self, valorQualquer):
        aux = self.primeiro
        if aux is not None:
            # Se já tem elemento
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = self.criarNovoElemento(valorQualquer)
        else:
            # Lista vazia
            self.primeiro = self.criarNovoElemento(valorQualquer)

    def removeElementoNoFinal(self):
        aux = self.primeiro
        if aux is not None:
            # Se tiver 2 ou mais elementos
            if aux.proximo is not None:
                while aux.proximo.proximo is not None:
                    aux = aux.proximo
                del(aux.proximo)
                aux.proximo = None
            else:
                # Só tem um elemento
                del(aux)
                self.primeiro = None
                print("--- Lista Vazia novamente ---")
        else:
            print("--- Lista Vazia ---")

    def addElementoNoInicio(self, valorQualquer):
        aux = self.primeiro
        if aux is not None:
            novo = self.criarNovoElemento(valorQualquer)
            novo.proximo = self.primeiro
            self.primeiro = novo
        else:
            self.primeiro = self.criarNovoElemento(valorQualquer)

    def removeElementoNoInicio(self):
        aux = self.primeiro
        if aux is not None:
            self.primeiro = self.primeiro.proximo
            del(aux)
        else:
            print("--- Lista Vazia ---")

    def removeQualquerElemento(self, v):
        aux = self.primeiro
        if aux is not None:
            ant = self.primeiro
            while aux is not None:
                if aux.valor != v:
                    ant = aux
                    aux = aux.proximo
                else:
                    # Achou o elemento
                    if aux == self.primeiro:
                        self.removeElementoNoInicio()
                    elif aux.proximo is None:
                        self.removeElementoNoFinal()
                    else:
                        ant.proximo = aux.proximo
                        del(aux)
                    return  # Sai da função após remover
            print("--- Valor nao encontrado ---")
        else:
            print("--- Lista Vazia ---")

# MAIN

# Criando uma lista VAZIA
minhaLista = Lista()
minhaLista.addElementoNoFinal(91)
minhaLista.addElementoNoFinal(92)
minhaLista.addElementoNoFinal(93)
minhaLista.addElementoNoFinal(94)

minhaLista.imprimeLista()
print("---------------------")

minhaLista.removeQualquerElemento(100)  # Tentando remover um valor que não existe
minhaLista.imprimeLista()