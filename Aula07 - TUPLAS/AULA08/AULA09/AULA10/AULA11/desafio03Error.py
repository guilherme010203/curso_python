from math import sqrt

try:
    
    user = int(input("DIGITE UM NUMERO INTEIRO:   "))
    print(user)
    raiz =sqrt(user)

except ValueError:
    print("POR FAVOR DIGITE UM VALOR NUMERICO")
    
else:
    print(raiz)    

    

