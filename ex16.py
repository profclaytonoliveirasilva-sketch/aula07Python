def conceito(nota):
    if nota >= 9:
        return "A"
    elif nota >= 7:
        return "B"
    elif nota >= 5:
        return "C"
    else:
        return "D"

nota = float(input("Digite a nota (0 a 10): "))
print(f"Conceito: {conceito(nota)}")
