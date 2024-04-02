retaA = int(input("Digite o tamanho da metade da Reta A: "))
retaB= int(input("Digite o tamanho da metade da Reta B: "))
retaC = int(input("Digite o tamanho da metade da Reta C: "))

somaAB = retaA + retaB
somaAC = retaA + retaC
somaBC = retaB + retaC

if somaAB > retaC and somaAC > retaB and somaBC > retaA :
    print("foi possivel formar um Equilátero:")

elif   somaAC > retaA and somaBC > retaC and somaAB > retaA:
    print(f"foi possivel formar um Isósceles:")

elif  somaBC> retaB and somaAB > retaA and somaAC > retaC: 
    print(f"foi possivel formar um Escaleno")   