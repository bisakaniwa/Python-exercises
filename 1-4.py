print("Exercícios Python", str("- 1 a 4"))
print("Vamos descobrir sua média do ano? Digite a nota do primeiro bimestre e aperte enter.")
numero1 = int(input())

print("Agora digite a nota do segundo bimestre e aperte enter de novo.")
numero2 = int(input())

print("E no terceiro bimestre, você tirou quanto? Me diga e aperte enter!")
numero3 = int(input())

print("E nesse último bimestre, você tirou quanto? Digite e aperte enter para descobrir sua média anual!")
numero4 = int(input())

soma = numero1 + numero2 + numero3 + numero4
media = soma / 4
print("Sua média do ano é", str(media) + "!")
