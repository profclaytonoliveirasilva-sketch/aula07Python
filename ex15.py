def maior_numero(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))
print(f"O maior número é {maior_numero(x, y, z)}")


