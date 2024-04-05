soma = 0
quantidade_numeros = 0

while True:
    numerouser = int(input("Digite um numero (codigo de parada 999):  "))
    if numerouser== 999:
        break
    
    soma += numerouser
    quantidade_numeros += 1

print("Total de números digitados:", quantidade_numeros)
print("Soma dos números:", soma)