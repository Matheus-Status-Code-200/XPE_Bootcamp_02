print('\nFatorial em Python:')
numero = int(input("Fatorial de: ") )
resultado=1
count=1
while count <= numero:
    resultado *= count
    count += 1
print(resultado)
numero = int(input("Fatorial de: ") )
resultado=1
for n in range(1,numero+1):
    resultado *= n
print(resultado),'\n'