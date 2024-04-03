primeiroTermo = int(input("Digite o Primeiro Termo:  "))
razao = int(input("Digite a Razão:  "))
decimo = primeiroTermo + (10-1) * razao
for g in range(primeiroTermo, decimo + razao, razao):
      print('{}'.format(g), end= '-')
print("ACABOU")      