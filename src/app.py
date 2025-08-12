def printLinhas():
    print("-*-" * 15)

def PrintMenu():
    printLinhas()
    print("Welcome to the Menu!")
    print("1. Adcionar Elmento a lista")
    print("2. Remover Elementos da lista")
    print("3. Contar Elementos da lista")
    print("4. Imprimir Elementos da lista")
    print("5. Exit")
    printLinhas()
def Menu():
    while True:
        PrintMenu()
        choice = input("Please select an option (1-5): ")
        if choice == '1':
            print("Onde você deseja adicionar o elemento? | (1) Início | (2) Fim | (3) Posição específica |")
            add_choice = input("Enter your choice (1-3): ")
            value = input("Digite o valor do elemento que deseja adicionar: ")
            if add_choice not in ['1', '2', '3']:
                print("Escolha inválida, por favor tente novamente.")
                continue
            if add_choice == '1':
                print("Vocẽ escolheu adicionar o elemento no início da lista.")
                lista.adicionarNoInicio(value)
            elif add_choice == '2':
                print("Você escolheu adicionar o elemento no fim da lista.")
                lista.adicionarNoFim(value)
            elif add_choice == '3':
                position = input("Digite a posição onde deseja adicionar o elemento: ")
                print(f"Você escolheu adicionar o elemento na posição {position}.")
                lista.adicionarNaPosicao(value, int(position))
            else:
                print("Escolha inválida, por favor tente novamente.")
        elif choice == '2':
            print("Onde você deseja remover o elemento? | (1) Início | (2) Fim | (3) Posição específica |")
            remove_choice = input("Enter your choice (1-3): ")
            if remove_choice == '1':
                print("Você escolheu remover o elemento do início da lista.")
                lista.removerDoInicio()
            elif remove_choice == '2':
                print("Você escolheu remover o elemento do fim da lista.")
                lista.removerDoFim()
            elif remove_choice == '3':
                position = input("Digite a posição do elemento que deseja remover: ")
                print(f"Você escolheu remover o elemento na posição {position}.")
                lista.removerDaPosicao(int(position))
            else:
                print("Escolha inválida, por favor tente novamente.")
        elif choice == '3':
            print("Você escolheu contar os elementos da lista.")
            print(f"Total de {lista.contarElementos()} elementos na lista.")
        elif choice == '4':
            print("Você escolheu imprimir os elementos da lista.")
            lista.imprimirLista()
        elif choice == '5':
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
            
class Elemento:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo    
class Lista:
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
        
if __name__ == "__main__":
    lista = Lista()
    Menu()