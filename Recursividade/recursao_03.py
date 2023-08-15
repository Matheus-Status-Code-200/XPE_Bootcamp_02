print('\nFatorial recursivo: ')
def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = fatorial_recursivo(numero)
print(f"O fatorial de {numero} é {fatorial}\n")
