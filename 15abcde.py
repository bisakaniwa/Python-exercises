print("Exercício", str(15))
print("Olá! Desculpe a pergunta indelicada, mas quantos reais você ganha por hora?")
h = float(input())

print("E quantas horas você trabalhou nesse mês?")
hm = float(input())

print("Certo, com base nisso vou fazer alguns cálculos...")
a = h * hm
print("a) Seu salário bruto nesse mês é de R$" + str(a) + ".")
b = (a * 0.08)
print("b) Você vai pagar R$" + str(round(b, 2)), "para o INSS...")
c = (a * 0.05)
print("c) Você vai pagar R$" + str(round(c, 2)), "para o sindicato...")
d = a - b - c
print("d) Ou seja, na verdade, você só vai receber R$" + str(round(d)), "nesse mês :')")