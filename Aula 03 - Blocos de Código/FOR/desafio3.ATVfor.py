soma = 0
cont = 0

for numero in range(1,501, 2 ):
   if  numero  % 3 ==0:
       soma += numero
       cont += 1
print('A soma de todos os {} numeros solicitados sao {}'.format(cont, soma))
       
       
   