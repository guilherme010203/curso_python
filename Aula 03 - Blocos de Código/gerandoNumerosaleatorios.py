import random

nota1 = random.randint(1,10)
nota2 = random.randint(1,10)

media = (nota1 + nota2) / 2

media >= 7

print(media)

if media >= 7 :
    print(f"você foi aprovado")
else:
    print(f"você foi reprovado")