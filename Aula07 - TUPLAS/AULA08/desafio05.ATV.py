pessoas = 0
nome = 0
peso = 0

while True:
    lista = []
    listaPeso = []
    listaNome = []
    
    pessoas = input("digite um numero:  ")
    nome= (input("digite seu nome :  ")).upper()
    peso = int(input("digite seu peso :  "))
    

    continuar = input("Deseja continuar [S/N]:  ").upper()
    if continuar == "N":
     print("SAINDO")
     break
    print("CONTINUANDO")
    
    
    if pessoas == pessoas :
        pessoas+=1
        lista.append(pessoas)
        print(f"Numero de pessoas cadastradas no site sao de {pessoas}")
        
    
    elif peso == max(peso):
        listaPeso.append(peso)
        print(f"Os maiores pesos foram {peso}")
                
    elif peso == min(peso):
        listaPeso.append(peso)
        print(F"Os menores pesos foram {peso} ") 
    lista.sort ()
    listaNome.sort()
    listaPeso.sort()      
  
  
    
