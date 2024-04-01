notaProva = float(input("Digite a nota da prova:  "))
notaAtividade = float(input("Digite a nota da atividade:  "))

#nota da prova = 70% media final
#nota da atividade = 30% media final

mediaFinal = notaProva + notaAtividade
print(mediaFinal)

if mediaFinal >= 70 :
    print(f"APROVADO")
elif mediaFinal >= 50 and 60.90 :
    print(f"RECUPERAÇÃO")
else:
    print(f"REPROVADO")    
     