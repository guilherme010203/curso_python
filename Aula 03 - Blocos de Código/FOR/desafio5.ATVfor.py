soma = 0 
cont = 0

for numero1 in range (1,7):
    numero = int(input("Digite um {} numero :  ".format(numero1)))
    if numero % 2 ==0:
       soma += numero
       cont += 1
print('Você informou {} numeros PARES e a SOMA foi {}'.format(cont, soma))    