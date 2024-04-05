pessoas = 0
homem = 0
mulher = 0

while True:
    
    idade = int(input("digite sua idade:  "))
    sexo = input("digite seu sexo [M/F]:  ").upper()
    
    
    continuar = input("Deseja continuar [S/N]:  ").upper()
    if continuar == "N":
     print("SAINDO")
     break
    print("CONTINUANDO")
    
  
    
    if idade>18:
        pessoas+=1
        print(f"Numero de pessoas com mais 18 anos sao de {pessoas}")
          
    elif sexo == "M":
        homem+=1
        print(f"A quantidade de Homens cadastrados foram de {homem}")
                
    elif sexo == "F": 
         mulher+=1
         print(F"A quantidade de mulheres cadastradas com menos de 20 anos foram de {mulher} ") 
            
