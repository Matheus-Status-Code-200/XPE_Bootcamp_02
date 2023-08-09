lst1 = [1, 2, 3, 4, 5]
30
lst2 = []
# Lambda function to square number
temp = lambda i:i**2

print("\nLista e Função Lambda.\n")
print("Lista original: "+str(lst1)+"\n")

for i in lst1:
 # Add to lst2
 lst2.append(temp(i))

print("Lista usando lambda: "+str(lst2))
print("\n")