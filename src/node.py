# n1 = Node(1, None) -> Exemplo de como instanciar um objeto do tipo Node
class Node:
    # Método construtor __init__: Define como um objeto Node é criado.
    def __init__(self, value, next, previous):
        # self.value: armazena o dado ou valor do nó (ex: um número, texto, etc.).
        self.value = value
        # self.next: é o ponteiro que aponta para o próximo nó na lista.
        # Se for o último nó, ele aponta para None.
        self.next = next
        self.previous = previous  # Adicionando ponteiro para o nó anterior, se necessário.
        