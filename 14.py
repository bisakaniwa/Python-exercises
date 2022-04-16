print("Exercício", str(14))
print("Olá, João! Quantos quilos de peixe você pegou hoje?")
p = float(input())

if p <= 50:
    print("Hoje você não precisa pagar multa!")
else:
    m = (p - 50) * 4
    print("Oh não! Você vai ter que pagar R$" + str(m), "de multa...")