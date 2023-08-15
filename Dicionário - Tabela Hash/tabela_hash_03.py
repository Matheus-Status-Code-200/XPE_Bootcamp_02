print('\nColisão em Hash:\n')
hash_table = [None] * 10
print (hash_table)

def hashing_func(key):
 return key % len(hash_table)

print (hashing_func(10)) 
print (hashing_func(20)) 
print (hashing_func(25)) 

def insert(hash_table, key, value):
 hash_key = hashing_func(key)
 hash_table[hash_key] = value
 
insert(hash_table, 10, 'Nepal')
print (hash_table,'\n')

insert(hash_table, 25, 'USA')
print (hash_table,'\n')

insert(hash_table, 20, 'India')
print (hash_table,'\n')