class Elemento:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo   
        
class Pilha:
    def __init__(self, primeiro=None):
        self.primeiro = primeiro

    # Fábrica de criar novos elementos:
    def criarNovoElemento(self, valorQualquer):
        e = Elemento(valorQualquer, None)
        return e

    def push(self, valorQualquer):
        aux = self.primeiro
        if aux is not None:
            novo = self.criarNovoElemento(valorQualquer)
            novo.proximo = self.primeiro
            self.primeiro = novo
        else:
            self.primeiro = self.criarNovoElemento(valorQualquer)

    def pop(self):
        aux = self.primeiro
        if aux is not None:
            self.primeiro = self.primeiro.proximo
            del(aux)
        else:
            print(f"\n")
            print("--- Pilha Vazia ---")
            
    def top(self):
        if self.primeiro is not None:
            print(f"\n")
            print(f"Top: {self.primeiro.valor}") 
            print(f"\n")
        else:
            print(f"\n")
            print("--- Pilha Vazia ---")
            return None
            
    def esvaziar(self):
        aux = self.primeiro
        print(f"\n")
        while aux is not None:
            print(f"Desempilhando: {aux.valor}")
            self.pop()
            aux = aux.proximo        
            
    def exibePilha(self):
        aux = self.primeiro
        if aux is not None:
            print(f"Fila: ")
            while aux is not None:    
                print(aux.valor)
                aux = aux.proximo
        else:
            print(f"\n")
            print("--- Pilha Vazia ---")

pilha = Pilha()

pilha.push(10)
pilha.push(20)
pilha.push(30)
pilha.push(40)
pilha.push(50)
pilha.push(60)
pilha.push(70)
pilha.push(80)
pilha.exibePilha()
pilha.top()
pilha.pop()
pilha.exibePilha()
pilha.top()
pilha.esvaziar()
pilha.exibePilha()