# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura *altura)
    return imc

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 16.9:
        return "Muito abaixo do peso"
    elif 17 <= imc <= 18.4:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Acima do peso"
    elif 30 <= imc <= 34.9:
        return "Obesidade grau I"
    elif 35 <= imc <= 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

# Programa principal
print("=== Cálculo de IMC ===")

n = int(input("Digite o número de pessoas: "))

for i in range(1, n + 1):
    print(f"--- Pessoa {i} ---")
    peso = float(input("Digite o peso (kg): ").replace(",", "."))
    altura = float(input("Digite a altura (m): ").replace(",", "."))
    
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    
    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")

print("=== Fim do programa ===")


