def preco_ingresso(idade):
    if idade < 12:
        return 10
    elif idade <= 18:
        return 15
    else:
        return 20

idade = int(input("Digite a idade: "))
print(f"Valor do ingresso: R$ {preco_ingresso(idade)}")


