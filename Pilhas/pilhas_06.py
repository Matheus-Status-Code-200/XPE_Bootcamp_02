import queue
#criando a fila
print("\nFila com queue.")
fila = queue.Queue()
#adicionando elementos
fila.put('Elemento 1')
fila.put('Elemento 2')
fila.put('Elemento 3')
#obtendo o tamanho da fila
tamanho = fila.qsize()
print("\nTamanho da Fila:", tamanho)
#removendo elementos
from time import sleep
print("Removendo elementos da fila:")
sleep(1)

while not fila.empty():
    print(fila.get())
    sleep(0.8)
#verificando se a fila esta vazia
esta_vazia = fila.empty()
print("A fila esta vazia?", esta_vazia)
print("\n")
