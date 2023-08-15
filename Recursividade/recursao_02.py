print('\nRecursividade em uma lista:')
def Soma_elementos(V, N):
    if N == 0:
        return V[N]
    else:
        return V[N] + Soma_elementos(V, N - 1)

V = [2, 10, 5, 7, 8, 11]
N = len(V) - 1  # Índice do último elemento do vetor

resultado = Soma_elementos(V, N)
print("\nA soma dos elementos da lista é:", resultado,'\n')
print(type(V))