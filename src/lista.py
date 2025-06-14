from node import Node

class List:
    # __init__ método construtor: recebe os atributos iniciais da classe
    def __init__(self):
        # 'first' é a cabeça (head) da lista, o ponto de partida. Começa como None (vazio).
        self.first = None

    #fabrica de criar novos elementos:
    def newNode(self, anyValue):
        # Cria uma instância da classe Node e a retorna. Simplifica a criação de elementos.
        n = Node(anyValue, None)
        return n
    
    #impressora de elementos da lista:
    def printList(self):
        # Verifica se a lista está vazia para evitar erros.
        if self.first is None: # -> se o primeiro elemento (nó) for nulo, a lista está vazia
            print("A lista está vazia")
            return
        
        # 'here' é uma variável auxiliar para percorrer a lista sem perder a referência do início.
        here = self.first 
        # O laço continua enquanto 'here' não for None, ou seja, até o último elemento (nó).
        while here:
            print(f"-> {here.value}")
            # Move o ponteiro 'here' para o próximo elemento (nó) da sequência.
            here = here.next
            
    #insersor de elemento (nó) ao final de lista
    def addToEnd(self, value):
        # Usa a o criador de elementos para criar um novo nó com o valor fornecido.
        new_node = self.newNode(value)
        
        # CASO 1: Se a lista está vazia, o novo nó se torna o primeiro.
        if self.first is None:
            self.first = new_node
            return # A operação termina aqui.
        
        # CASO 2: A lista já tem elementos. É preciso encontrar o último.
        last = self.first
        # O laço avança na lista até que 'last.next' seja None, indicando que 'last' é o último nó.
        while last.next:
            last = last.next
            
        # O 'next' do antigo último nó agora aponta para o novo nó.
        last.next = new_node
        
    #contador de elementos
    def counterList(self):
        # Se a lista não tem um primeiro elemento (nó), ela tem 0 elementos.
        if self.first is None:
            return 0
        
        # Inicia um contador para somar os nós.
        counter = 0
        # Variável auxiliar para percorrer a lista.
        here = self.first
        
        # Percorre todos os nós da lista.
        while here:
            # Incrementa o contador para cada nó encontrado.
            counter += 1
            # Avança para o próximo nó.
            here = here.next
            
        # Retorna o total de nós contados.
        return counter
    
    #insersor de elemento (nó) ao início da lista
    def addBegin(self, value):
        # Cria o novo nó que será adicionado.
        new_node = self.newNode(value)
        
        # O 'next' do novo nó deve apontar para quem era o primeiro anteriormente.
        new_node.next = self.first
        
        # Atualiza a cabeça da lista ('first') para ser o novo nó.
        self.first = new_node
        
        
##------------------------------------------------##
## MAIN - Bloco de Testes dos Métodos ##

print("INICIANDO TESTES...")
newList = List()

# Teste 1: Adicionar elementos ao final da lista.
print("\n1. Adicionando 10, 20 e 30 ao final:")
newList.addToEnd(10)
newList.addToEnd(20)
newList.addToEnd(30)
newList.printList() # Saída esperada: -> 10 -> 20 -> 30

# Teste 2: Contar os elementos da lista.
print(f"Quantidade de elementos na lista: {newList.counterList()}") # Saída esperada: 3

# Teste 3: Adicionar um elemento (nó) no início.
print("\n2. Adicionando 99 ao início:")
newList.addBegin(99)
newList.printList() # Saída esperada: -> 99 -> 10 -> 20 -> 30
print(f"Nova quantidade de elementos: {newList.counterList()}") # Saída esperada: 4

# Teste 4: Operações em uma lista vazia.
print("\n3. Testando uma lista vazia:")
otherList = List()
otherList.printList() # Saída esperada: A lista está vazia
print(f"Quantidade de elementos na outra lista: {otherList.counterList()}") # Saída esperada: 0