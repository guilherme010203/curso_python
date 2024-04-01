ValorDacasa = int(input("digite o valor da casa:  "))
print(ValorDacasa)

SalarioDocomprador = int(input("digite seu salário:  "))
print(SalarioDocomprador)

AnosApagar = int(input("em quantos anos você quer pagar a casa:  "))
print(AnosApagar)

tempo = AnosApagar*12

prestaçãoMensal = ValorDacasa / tempo

prestaçãoPercentual = SalarioDocomprador *0.3

print(prestaçãoPercentual)

if  prestaçãoMensal <= prestaçãoPercentual :
    print(f"O emprestimo foi aprovado")
else:
    print(f"O emprestimo foi reprovado")