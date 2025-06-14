# n1 = Node(1, None) -> Exemplo de como instanciar um objeto do tipo Node
class Node:
    # Método construtor __init__: Define como um objeto Node é criado.
    def __init__(self, value, next):
        # self.value: armazena o dado ou valor do nó (ex: um número, texto, etc.).
        self.value = value
        # self.next: é o ponteiro que aponta para o próximo nó na lista.
        # Se for o último nó, ele aponta para None.
        self.next = next

    # Método para tentar percorrer e imprimir a lista a partir do nó atual.
    # ATENÇÃO: Esta é uma forma incomum e com falhas de percorrer a lista.
    def LacoDoFimDoMundo(self):
        # O laço continua enquanto o ponteiro 'next' do nó atual não for nulo.
        # Isso faz com que ele pare no penúltimo elemento, sem imprimir o último.
        while (self.next != None):
            print(self.value)
            # A linha "self = self.next" altera apenas a referência local 'self'
            # dentro deste método, não alterando a lista de fato.
            # A forma correta de percorrer a lista fica na classe 'List'.
            self = self.next

    # Método que realiza uma operação com o valor do próprio nó.
    def QuadradoValor(self): # -> self: referência para o próprio objeto
        # Retorna o valor do nó multiplicado por ele mesmo (ao quadrado).
        return (self.value * self.value)