# Funções matemáticas
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

def media(a, b):
    return (a + b) / 2

# Programa principal
print("=== Calculadora de Operações com Dois Números ===")

# Entrada de dados
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Cálculos
soma = somar(num1, num2)
subtracao = subtrair(num1, num2)
multiplicacao = multiplicar(num1, num2)
divisao = dividir(num1, num2)
media_valor = media(num1, num2)

# Saída de resultados
print("--- Resultados ---")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Média: {media_valor}")

