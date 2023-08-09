# Lista, Array e Fila em Python

...

## Lista

...

Operações comuns em listas:
- Acesso a elementos por índice: `fruits[0]` retorna "Apple".
- Adição de elementos: `fruits.append("Orange")` adiciona "Orange" ao final da lista.
- Remoção de elementos: `fruits.remove("Mango")` remove "Mango" da lista.
- Tamanho da lista: `len(fruits)` retorna o número de elementos.

## Array

Em Python, um array é uma estrutura de dados similar a uma lista, mas é geralmente utilizado quando se trabalha com grandes conjuntos de dados numéricos. A biblioteca NumPy é comumente utilizada para lidar com arrays multidimensionais e operações matemáticas.

### Operações comuns em arrays:

- Operações matemáticas: 
  - NumPy permite realizar operações em todos os elementos do array de uma vez.
  - Indexação e fatiamento: Similar às listas, é possível acessar elementos específicos e criar subarrays.
  ...

## Fila

Uma fila é uma estrutura de dados que segue a regra do "primeiro a entrar, primeiro a sair" (FIFO - First-In-First-Out). Em Python, isso pode ser implementado utilizando a classe queue.Queue da biblioteca padrão.

### Operações comuns em uma filas:

- put(item): Adiciona um item no final da fila.
- get(): Remove e retorna o item do início da fila.
- empty(): Verifica se a fila está vazia.
