# Usando LISTA
numeros_lista = [i for i in range(101)]
print("Lista de números de 0 a 100:")
print(numeros_lista)

# Usando TUPLA
numeros_tupla = tuple(i for i in range(101))
print("Tupla de números de 0 a 100:")
print(numeros_tupla)

# Usando SET
numeros_set = {i for i in range(101)}
print("Set de números de 0 a 100:")
print(numeros_set)

# Usando DICT
numeros_dict = {i: i for i in range(101)}
print("Dict de números de 0 a 100:")
print(numeros_dict)