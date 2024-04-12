dicionario = {}
lista = list()
import random
dicionario['dado1'] = random.randint(1,12)
dicionario['dado2'] = random.randint(1,12)
dicionario['dado3'] = random.randint(1,12)
dicionario['dado4'] = random.randint(1,12)

if dicionario['dado1'] > dicionario['dado2']<dicionario['dado1']>dicionario['dado3']<dicionario['dado1']>dicionario['dado4']:
    print('O JOGADOR 1 TIROU O MAIOR NUMERO')
    
 
elif  dicionario['dado2'] > dicionario['dado3']<dicionario['dado2']>dicionario['dado4']<dicionario['dado2']>dicionario['dado1']:
    print('O JOGADOR 2 TIROU O MAIOR NUMERO') 
   
elif  dicionario['dado3'] > dicionario['dado4']<dicionario['dado3']>dicionario['dado2']<dicionario['dado3']>dicionario['dado1']:
    print('O JOGADOR 3 TIROU O MAIOR NUMERO')
 
elif dicionario['dado4']>dicionario['dado3']<dicionario['dado4']>dicionario['dado2']<dicionario['dado4']>icionario['dado1']:
    print('O JOGADOR 4 TIROU O MAIOR NUMERO')   
  
    
    

           
lista.append(dicionario.copy()) 
print(lista)        