dicionario = {}
lista = list()

dicionario['nome'] =(input('DIGITE SEU NOME:  '))
    
notaProv= int(input('DIGITE A NOTA DA PROVA:  '))
    
notaATV= int(input('DIGITE A NOTA DA ATIVIDADE:  '))
dicionario["mediaFinal"] = (notaProv + notaATV) /2
    
if dicionario["mediaFinal"] >7:
    dicionario["Resultado"] = 'APROVADO'
    
elif dicionario["mediaFinal"] >=5:
    dicionario['resultado'] = 'RECUPERAÇÃO' 
else:
    dicionario['resultado']  = 'REPROVADO'
    
lista.append(dicionario.copy()) 
print(lista)