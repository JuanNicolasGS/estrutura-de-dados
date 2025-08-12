

class Elemento:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo    

class Fila:
    def __init__(self):
        self.ultimo = None
        self.primeiro = None

    def criarNovoElemento(self, valor):
        e = Elemento(valor)
        return e

    def enfileirar(self, valor):
        aux = self.primeiro
        if aux is not None:
            # Se já tem elemento
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = self.criarNovoElemento(valor)
        else:
            # Lista vazia
            self.primeiro = self.criarNovoElemento(valor)

    def desenfileirar(self):
        if self.primeiro is None:

            print("Fila vazia")
            return
        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None

    def imprimeFila(self):
        aux = self.primeiro
        if aux is not None:
            print(f"Fila: \n")
            while aux is not None:
                print(aux.valor)
                aux = aux.proximo
            print(f"\n")
        else:
            print(f"\n")
            print("--- Fila Vazia ---")
            
    def esvaziar(self):
        aux = self.primeiro
        while aux is not None:
            print(f"Desenfileirando: {aux.valor}")
            self.desenfileirar()
            aux = aux.proximo
    
    def verificarPrimeiro(self):
        if self.primeiro is not None:
            print(f"Primeiro: {self.primeiro.valor}")
            print(f"\n")
        else:

            print(f"\nFila vazia")
        
fila = Fila()
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
fila.enfileirar(40)
fila.enfileirar(50)
fila.enfileirar(60)
fila.imprimeFila()
fila.desenfileirar()
fila.imprimeFila()
fila.verificarPrimeiro()
fila.esvaziar()
fila.imprimeFila()