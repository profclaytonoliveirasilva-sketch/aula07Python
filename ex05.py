# Função para calcular o desconto do INSS
def calcularInss(inss):
    if salarioBruto >= 1800:
        inss = salarioBruto * 0.11
    else:
        inss = salarioBruto * 0.09
    
    return inss
    

# Função para calcular o desconto do Vale-Transporte
def calcularVale(vale):
    if salarioBruto >= 1500:
        vale = salarioBruto * 0.06
    else:
        vale = salarioBruto * 0.05
    
    return vale

# Função para calcular o Bônus
def calcularBonus(bonus):
    if salarioBruto >= 1240:
        bonus = 700
    else:
        bonus = 500
    
    return bonus

# Função para classificar o Cargo
def classificarCargo(cargo):
    if salarioBruto >= 3000:
        cargo = "Acionista"        
    elif salarioBruto >= 2000:
        cargo = "Gerente"
    else:
        cargo = "Vendedor"
    
    return cargo


# Função para calcular o salário líquido
def salarioLiquido(salarioLiquido):
    salarioLiquido = salarioBruto - (calcularInss(inss) + calcularVale(vale)) + calcularBonus(bonus)
    return salarioLiquido

# Programa principal
print("=== Cálculo de Salário ===")

nome = input("Digite o nome do funcionário: ")
salarioBruto = float(input("Digite o salário bruto: R$ "))

# Cálculos
inss = calcularInss(salarioBruto)
vale = calcularVale(salarioBruto)
bonus = calcularBonus(salarioBruto)
cargo = classificarCargo(salarioBruto)
salarioLiquido = salarioLiquido(salarioBruto)
    

# Exibição dos resultados
print("--- Folha de Pagamento ---")
print(f"Nome: {nome}")
print(f"Cargo: {cargo}")
print(f"Salário Bruto: R$ {salarioBruto:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto Vale-Transporte: R$ {vale:.2f}")
print(f"Bônus: R$ {bonus:.2f}")
print(f"Salário Líquido: R$ {salarioLiquido:.2f}")

print("=== Fim do Programa ===")

