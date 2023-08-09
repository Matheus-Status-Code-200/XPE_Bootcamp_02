class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None


class Pilha:
    
    def __init__(self):
        print("\nPilhas com Estruturas Encadeadas.\n")
        self.topo = None

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo

    def remove(self):
        assert self.topo, "Impossível remover valor de pilha vazia."
        self.topo = self.topo.anterior

    def __str__(self):
        if self.topo is None:
            return "Pilha vazia"
        
        elementos = []
        nodo_atual = self.topo
        while nodo_atual is not None:
            elementos.append(str(nodo_atual.dado))
            nodo_atual = nodo_atual.anterior
        return " -> ".join(elementos) + " -> None"

pilha = Pilha()
print("Pilha vazia:", pilha)

from time import sleep
for i in range(5):
    pilha.insere(i)
    sleep(0.7)
    print(f"Inserindo o valor {i} no topo da pilha: [{pilha}]")
print('\n')
while pilha.topo is not None:
    pilha.remove()
    sleep(0.7)
    print(f"Removendo elemento do topo da pilha: [{pilha}]")
print('\n')
