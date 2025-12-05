def verificar_numero(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"

# Teste
numero = int(input("Digite um número: "))
print(verificar_numero(numero))
