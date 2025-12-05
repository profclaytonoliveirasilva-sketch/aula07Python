def faixa_etaria(idade):
    if idade < 13:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "Melhor idade"

idade = int(input("Digite a idade: "))
print(faixa_etaria(idade))


