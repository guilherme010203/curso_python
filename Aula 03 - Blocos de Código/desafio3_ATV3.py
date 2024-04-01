distancia = int(input("digite a distancia:  "))

precoPassagem = (distancia *0.50) 

precoPassagem2 = (distancia *0.45) 

if distancia <= 200:
    print(f"Você ira pagar {precoPassagem} R$")
else:
    print(f"Você ira pagar {precoPassagem2} R$")    