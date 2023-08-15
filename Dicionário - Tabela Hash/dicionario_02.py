print('\nUsando os métodos(get, items, keys, values e pop) do tipo Dict:')

dicionario = {
 'nome': 'Ana',
 'idade': 25,
 'cidade': 'São Paulo'
 }
# Usando get
print("dict_get ",dicionario.get('nome'))
# Usando item
print(dicionario.items())
# Usando key
print(dicionario.keys())
# Usando values
print(dicionario.values())
# Usando pop
print(dicionario.pop('idade'),'\n')