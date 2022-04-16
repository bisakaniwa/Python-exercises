print("Exercício", str(11))
print("Vamos calcular mais algumas coisas? Primeiramente, digite um número inteiro e aperte",
      "enter.")
i1 = int(input())

print("Ótimo, agora mais um número inteiro e enter de novo.")
i2 = int(input())

print("OK, agora um número real. Não se esqueça do enter!")
r = float(input())

print("OK, agora vamos calcular.")
a = i1 * 2 / (i2 / 2)
print("a) O dobro do primeiro dividido pela metade do segundo é", str(a))
b = (i1 * 3) + r
print("b) A soma do triplo do primeiro com o terceiro é", str(b) + ".")
c = r ** 3
print("c) O terceiro elevado ao cubo é", str(c) + ".")