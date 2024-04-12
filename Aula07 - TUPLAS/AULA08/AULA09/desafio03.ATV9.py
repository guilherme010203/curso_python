dicionario = {}
lista = list()

dicionario['nome'] =(input('DIGITE SEU NOME:  '))
    
dicionario['datadenacimento']= int(input('DIGITE O ANO DE NASCIMENTO:  '))

dicionario['carteiradetrabalho']= int(input('DIGITE O NUMERO DA CARTEIRA DE TRABALHO, (SE VOCÊ NAO TIVER DIGITE 0):   '))

dicionario['salario'] = int(input('DIGITE SEU SALÁRIO:     '))

dicionario['contratacao'] = int(input('DIGITE SEU ANO DE CONTRATAÇÃO:   '))

if dicionario['carteiradetrabalho'] ==0:
    print('DESCULPE, VOCÊ NAO TEM CARTEIRA DE TRABALHO')

 
if dicionario['carteiradetrabalho']>0:
    print(f'PARABÉNS VOCÊ TEM CARTEIRA DE TRABALHO, VOCÊ IRA SE APOSENTAR EM {dicionario["contratacao"] + 35}')
    
lista.append(dicionario.copy()) 
print(lista)    


    
    
     