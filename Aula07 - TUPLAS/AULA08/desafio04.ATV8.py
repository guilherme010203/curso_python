lista=[]
listaPar =lista %2
listaImpar = lista %3
while True:
    numero = str(input("DIGITE UM VALOR, ou 'N' PARA PARAR:    "))
    if numero.upper== "N":
        break
    if int(numero) in lista:
        
        print(f"O NUMERO {int(numero)} JÁ FOI ADICIONADO")
    else:
        lista.append(int(numero))
        
           
        
        
lista.sort() 
 
print(f"OS VALORES DA LISTA FORAM {lista}")
    
if listaPar == 0:
    print(F"OS VALORES PARES DA LISTA FORAM {listaPar}")    
     
if listaImpar == 1:
    print(f"OS VALORES IMPARES DA LISTA FORAM {listaImpar}")






