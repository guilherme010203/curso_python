retaA = int(input("Digite o tamanho da metade da Reta A: "))
retaB= int(input("Digite o tamanho da metade da Reta B: "))
retaC = int(input("Digite o tamanho da metade da Reta C: "))

somaAB = retaA + retaB
somaAC = retaA + retaC
somaBC = retaB + retaC

if somaAB > retaC and somaAC > retaB and somaBC > retaA :
    print("foi possivel formar um Equilátero:")

if retaA == retaB == retaC:
    print("o triangulo formado foi o Equilátero")
    
elif retaA != retaB != retaC != retaA:
     print("o triangulo formado Escaleno")   
     
else:
    print("o triangulo formado foi o Isósceles:")     