import numpy as np

print('\nMétodo Shift:\n')
print('Utilizando np.roll() para realizar um deslocamento circular (ou shift) nos elementos do array.')
print('Isso significa que os elementos do array serão deslocados para a direita por 3 posições,')
print('e os elementos que "caírem" fora do final serão trazidos de volta para o início.\n')

array = np.array([1, 2, 3, 4, 5])

array_new = np.roll(array, 1)
print(array_new)
print('\n')
array_new = np.roll(array, 2)
print(array_new)
print('\n')
array_new = np.roll(array, 3)
print(array_new)
print('\n')
