class Nodo:
    """Esta classe representa um nodo de uma estrutura duplamente encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'

class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada."""
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return f'[{self.primeiro}]'

    def insere(self, novo_dado):
        """Insere um elemento no final da fila."""
        novo_nodo = Nodo(novo_dado)
        if self.primeiro is None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def remove(self):
        """Remove o primeiro elemento da fila."""
        assert self.primeiro is not None, "Impossível remover elemento de fila vazia."
        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None

# Cria uma fila vazia.
fila = Fila()
print("\nLimpando Elementos da Fila Encadeada:\n")
print("Fila vazia:", fila)

# Insere elementos na fila.
for i in range(5):
    fila.insere(i)
    print(f"Inserindo o valor {i} no final da fila: {fila}")

# Remove elementos da fila.
while fila.primeiro is not None:
    fila.remove()
    print(f"Removendo elemento que está no começo da fila:", fila)

print('\n')
