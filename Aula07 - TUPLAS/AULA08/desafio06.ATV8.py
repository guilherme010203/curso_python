def separar_pares_impares(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

def main():
    numeros = []

    while True:
        try:
            numero = str(input("Digite um número (ou digite 'N' para parar): "))
            if numero.upper == 'N':
                break
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite apenas números inteiros.") 
              
pares, impares = separar_pares_impares()
for i in range(0,7):
    numero = int(input("DIGITE UM VALOR:   "))
    
    



    
    print("Números pares:", pares)
    print("Números ímpares:", impares)


 