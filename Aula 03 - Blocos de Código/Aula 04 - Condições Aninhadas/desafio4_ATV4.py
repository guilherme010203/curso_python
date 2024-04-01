dataDenascimento = int(input("digite seu ano de nascimento:  "))
anoAtual = int(input("digite o ano atual:  "))

Resultado = anoAtual - dataDenascimento
print(Resultado)

if Resultado <= 9 :
    print(f"MIRIM")

    
elif Resultado <= 14 :
    print(f"INFANTIL") 

           
elif Resultado <= 19 : 
    print(f"JUNIOR") 

    
  
elif Resultado <=24:
    print(f"SÊNIOR") 

     
elif Resultado >= 25:
    print(f"MASTER")    