print("Exercícios", str(12), "e", str(13))
print("Vamos descobrir seu peso ideal? Me diga a sua altura em metros e aperte enter.")
h = float(input())

print("Agora me informe seu sexo biológico. Digite m para masculino ou f para feminino, depois aperte enter!")
m = (72.7 * h) - 58
f = (62.1 * h) - 44.7
input()

if input == m:
    print("Seu peso ideal é aproximadamente", str(round(m, 2)) + "kg!")
elif input == f:
    print("Seu peso ideal é aproximadamente", str(round(f, 2)) + "kg!")
else:
    print("Ei! Não é pra digitar isso!")
