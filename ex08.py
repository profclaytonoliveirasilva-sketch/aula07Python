# Função que retorna o maior valor da lista
def maior_valor(lista):
    return max(lista)

# Função que retorna o menor valor da lista
def menor_valor(lista):
    return min(lista)

# Função que retorna o tamanho da lista
def tamanho_lista(lista):
    return len(lista)

# Programa principal
def main():
    print("=== Análise de Lista de Números ===")
    numeros = []

    # Entrada de 10 números inteiros
    for i in range(10):
        n = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(n)

    # Mostrando os resultados
    print("=== Resultados ===")
    print("Números digitados:", numeros)
    print("Maior valor:", maior_valor(numeros))
    print("Menor valor:", menor_valor(numeros))
    print("Tamanho da lista:", tamanho_lista(numeros))

# Chama o programa principal
main()

