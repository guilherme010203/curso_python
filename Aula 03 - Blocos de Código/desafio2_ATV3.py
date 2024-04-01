
velocidade = int(input("digite um valor:  ") )

multa = (velocidade - 80) *7

if velocidade > 80:
    print(f"Você foi multado, valor a pagar {multa}")
else:
    print(f"Você não foi multado " )    
    