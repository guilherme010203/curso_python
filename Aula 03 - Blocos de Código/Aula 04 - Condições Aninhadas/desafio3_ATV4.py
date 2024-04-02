notaProva = float(input("Digite a nota da prova de 0 a 100:  "))
notaAtividade = float(input("Digite a nota da atividade de 0 a 100:  "))

#nota da prova = 70% media final
#nota da atividade = 30% media final

    
mediaFinal = (notaProva + notaAtividade) /2

if mediaFinal >= 70 :
    print(f"APROVADO")
    
elif mediaFinal >= 50 and 60.90 :
    print(f"RECUPERAÇÃO")
    
elif mediaFinal < 50:
    print(f"REPROVADO")    
     
    