import heapq
print("\nFila de Prioridades com Heap:")
print("Os números em heapq.heappush(fila, (4, 'A') representam sua prioridade,")
print("quanto menor mais prioridade vai ter independente do momento da entrada na fila .\n")

fila = []
# Inserindo elementos na fila de prioridades
heapq.heappush(fila, (4, 'A'))
heapq.heappush(fila, (3, 'B'))
heapq.heappush(fila, (2, 'C'))
heapq.heappush(fila, (1, 'D'))
heapq.heappush(fila, (5, 'E'))

# Removendo elementos da fila de prioridades
print(heapq.heappop(fila)) 
print(heapq.heappop(fila)) 
print(heapq.heappop(fila)) 
print(heapq.heappop(fila)) 
print(heapq.heappop(fila)) 
print('\n')