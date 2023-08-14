# isso cria um conjunto vazio
conjunto_A = set()
# isso cria um conjunto com valores
conjunto_B = {1, 2, 3, 4, 5}
# isso adiciona um elemento ao conjunto
conjunto_A.add(10)
# isso cria um conjunto com valores
conjunto_C = {3, 4, 5, 6, 7}

print('\nOperações com conjuntos')

conjunto_uniao = conjunto_B | conjunto_C

conjunto_diferenca = conjunto_B - conjunto_C

conjunto_interseccao = conjunto_B & conjunto_C

conjunto_diferenca_simetrica = conjunto_B ^ conjunto_C
print('\nUnião de Conjunto')
print(conjunto_uniao)
print('\nDiferenca de Conjunto')
print(conjunto_diferenca)
print('\nIntersecção de Conjunto')
print(conjunto_interseccao)
print('\nDiferença simétrica de Conjunto')
print(conjunto_diferenca_simetrica,'\n')