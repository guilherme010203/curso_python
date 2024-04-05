import random
tentativas = 0
while True:
    
    
    n1 = int(input("Digite um numero de 0 a 10:   "))
    n2 = random.randint(0,10)
    print(n2)
    if n1==n2:
        print(f"Parabéns você venceu seus palpites foram  {tentativas}")
        break
         
    else:
        print("Você perdeu, tente novamente") 
        tentativas+=1
        
    if tentativas:
       print(f"Seus palpites foram {tentativas}") 
        
    
        
        
        
    
    
