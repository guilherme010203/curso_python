n1 = int(input('digite um numero:   '))
n2 = int(input('digite um numero:   '))

divisao = n1/n2
print(divisao)

try:
   divisao == (n1/n2)==0
   print(divisao) 
except  ZeroDivisionError:
    print("DESCULPE, NAO EXISTE DIVISAO POR ZERO")
       

    
      
     