import random

def gerar_dados(qtd, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(qtd)]

# Programa principal
print("=== Gerador de Dados Aleatórios ===")

# Entrada de dados
qtd = int(input("Quantos números deseja gerar? "))
min_val = int(input("Digite o valor mínimo: "))
max_val = int(input("Digite o valor máximo: "))

# Geração da lista
numeros = gerar_dados(qtd, min_val, max_val)

# Exibição dos resultados
print("\n--- Números Gerados ---")
print(numeros)

print("\n=== Fim do Programa ===")