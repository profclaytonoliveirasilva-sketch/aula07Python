# Função para calcular a multa
def calcular_multa(peso):
    limite = 100  # limite estabelecido pelo regulamento
    valor_multa = 4.00  # valor da multa por quilo excedente
    
    if peso > limite:
        excesso = peso - limite
        multa = excesso * valor_multa
        return excesso, multa
    else:
        return 0, 0  # sem excesso nem multa

# Programa principal
print("=== Controle de Produtividade do Pescador ===")

# Entrada de dados
peso_peixes = float(input("Digite o peso total de peixes pescados (em kg): "))

# Cálculo
excesso, multa = calcular_multa(peso_peixes)

# Saída de resultados
print("--- Resultado ---")
if excesso > 0:
    print(f"Peso excedente: {excesso:.2f} kg")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Dentro do limite permitido. Nenhuma multa a pagar.")


