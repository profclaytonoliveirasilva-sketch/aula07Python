def desconto(valor):
    if valor >= 500:
        return valor * 0.09  
    elif valor >= 200:
        return valor * 0.08  
    else:
        return valor*  0.07

preco = float(input("Digite o valor do produto: "))
print(f"Preço com desconto: R$ {desconto(preco):.2f}")


