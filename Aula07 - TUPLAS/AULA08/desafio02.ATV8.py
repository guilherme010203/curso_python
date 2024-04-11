lista=[]

while True:
    numero = int(input("DIGITE UM VALOR, ou 'N' PARA PARAR:    ").upper())
    
    if numero == "N":
        break
    if int(numero) in lista:
        
        print(f"O NUMERO {int(numero)} JÁ FOI ADICIONADO")
        
    else:
        lista.append(int(numero))
        
lista.sort() 

print(f"OS VALORES DIGITADOS EM ORDEM CRECENTE FORAM{lista}")
           