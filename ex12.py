def par_ou_impar(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

num = int(input("Digite um número: "))
print(par_ou_impar(num))


