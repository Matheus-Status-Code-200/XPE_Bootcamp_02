# Inicia uma pilha – vazia
def init(P):
    print("\nEmpilha e desempilha os elemento na pilha:\n")
    P = []
# Empilha novo elemento
def push(P, x):
    P.append(x)
# Retorna o elemento do topo da pilha mas não desempilha
def top(P):
    return None if is_empty(P) else P[-1]
# Remove elemento do topo da pilha
def pop(P):
    return None if is_empty(P) else P.pop()
# retorna True se a pilha está vazia
def is_empty(P):
    return len(P) == 0
# Empilha e imprime o estado atual da pilha
def Empilha(p, z):
    push(p, z)
    print(p)
# Desempilha e imprime o estado atual da pilha
def Desempilha(p):
    x = pop(p)
    if x is None: print("Vazia")
    else: print(p)
# inicia a pilha
mp = []
init(mp)
# operações
print("Empilhando:")
Empilha(mp, 1)
Empilha(mp, "tipo de elemento")
Empilha(mp, (5, 4, 3))
Empilha(mp, True)
print(f"Elemento mais acima da pilha: {top(mp)}")
print("\n")
print("Desempilhando.")
Desempilha(mp)
Desempilha(mp)
Desempilha(mp)
Desempilha(mp)
Desempilha(mp)
print(f"Elemento mais acima da pilha: {top(mp)}\n")
