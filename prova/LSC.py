class Elemento:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

class ListaCircular:
    def _init_(self):
        self.primeiro = None

    # Fábrica de criar novos elementos
    def criarNovoElemento(self, valorQualquer):
        e = Elemento(valorQualquer, None)
        return e

    def imprimeLista(self):
        aux = self.primeiro
        if aux is not None:
            while True:
                print(aux.valor)
                aux = aux.proximo
                if aux == self.primeiro:
                    break
        else:
            print("--- Lista Vazia ---")

    def addElementoNoFinal(self, valorQualquer):
        if self.primeiro is None:
            self.primeiro = self.criarNovoElemento(valorQualquer)
            self.primeiro.proximo = self.primeiro
        else:
            aux = self.primeiro
            while aux.proximo != self.primeiro:
                aux = aux.proximo
            novo = self.criarNovoElemento(valorQualquer)
            aux.proximo = novo
            novo.proximo = self.primeiro

    def removeElementoNoFinal(self):
        if self.primeiro is None:
            print("--- Lista Vazia ---")
            return

        if self.primeiro.proximo == self.primeiro:
            del(self.primeiro)
            self.primeiro = None
            print("--- Lista Vazia novamente ---")
        else:
            aux = self.primeiro
            while aux.proximo.proximo != self.primeiro:
                aux = aux.proximo
            del(aux.proximo)
            aux.proximo = self.primeiro

    def addElementoNoInicio(self, valorQualquer):
        if self.primeiro is None:
            self.primeiro = self.criarNovoElemento(valorQualquer)
            self.primeiro.proximo = self.primeiro
        else:
            novo = self.criarNovoElemento(valorQualquer)
            aux = self.primeiro
            while aux.proximo != self.primeiro:
                aux = aux.proximo
            novo.proximo = self.primeiro
            aux.proximo = novo
            self.primeiro = novo

    def removeElementoNoInicio(self):
        if self.primeiro is None:
            print("--- Lista Vazia ---")
        elif self.primeiro.proximo == self.primeiro:
            del(self.primeiro)
            self.primeiro = None
            print("--- Lista Vazia novamente ---")
        else:
            ultimo = self.primeiro
            while ultimo.proximo != self.primeiro:
                ultimo = ultimo.proximo
            aux = self.primeiro
            self.primeiro = self.primeiro.proximo
            ultimo.proximo = self.primeiro
            del(aux)

    def removeQualquerElemento(self, v):
        if self.primeiro is None:
            print("--- Lista Vazia ---")
            return

        aux = self.primeiro
        ant = None

        while True:
            if aux.valor == v:
                # Caso: único elemento
                if aux == self.primeiro and aux.proximo == self.primeiro:
                    del(self.primeiro)
                    self.primeiro = None
                    print("--- Lista Vazia novamente ---")
                    return

                # Caso: remover primeiro
                if aux == self.primeiro:
                    self.removeElementoNoInicio()
                    return

                # Caso: remover outro
                ant.proximo = aux.proximo
                del(aux)
                return

            ant = aux
            aux = aux.proximo

            if aux == self.primeiro:
                break

        print("--- Valor não encontrado ---")


# MAIN - exemplo de uso
if _name_ == "_main_":
    minhaLista = ListaCircular()
    minhaLista.addElementoNoFinal(91)
    minhaLista.addElementoNoFinal(92)
    minhaLista.addElementoNoFinal(93)
    minhaLista.addElementoNoFinal(94)

    minhaLista.imprimeLista()
    print("---------------------")

    minhaLista.removeQualquerElemento(100)  # Tentando remover valor inexistente
    minhaLista.imprimeLista()