prova = float(input("digite a nota na prova do aluno:  "))
atividade = float(input("digite a media da nota das atividades:  "))

#nota prova = 70% da media final
#nota atividades = 30% da media final

mediaFinal = prova + atividade
print(mediaFinal)

if mediaFinal >= 50:
    print("Aprovado")
elif mediaFinal >= 40:
    print("Recuperação")    
else:
    print("Reprovado")    