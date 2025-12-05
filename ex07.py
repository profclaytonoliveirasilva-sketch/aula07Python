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
    
    # Exemplo de lista
    numeros = [12, 45, 7, 89, 23, 5, 67]
    print("Lista de números:", numeros)
    
    print("\nResultados:")
    print("Maior valor:", maior_valor(numeros))
    print("Menor valor:", menor_valor(numeros))
    print("Tamanho da lista:", tamanho_lista(numeros))

# Chama o programa principal
main()
