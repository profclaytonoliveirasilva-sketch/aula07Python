def situacao_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

media = float(input("Digite a média do aluno: "))
print(situacao_aluno(media))
