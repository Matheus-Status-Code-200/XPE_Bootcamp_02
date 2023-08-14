A = {0, 1, 3, 5, 7, 9} 
B = {0, 2, 4, 6, 8}
C = A.union(B)
E = {2, 4, 6, 8}
print('Intersecção A intersection B')
D = A.intersection(B)
print(D)
print('\nDiferença A difference B ')
set4 = A.difference(B)
print(set4)
print('\nSimetria A^B')
simetrica = A ^ B
print(simetrica)
print('\nConjuntos (A B) Disjuntos:', A.isdisjoint(B))
print('\nConjuntos (A E) Disjuntos:', A.isdisjoint(E),'\n')