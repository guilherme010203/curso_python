from random import randint


maquina = 0
usuario = 0


aleatorio = randint(1,20)

for elemento in range(1,11):
    numero = int(input(f"{elemento}° Rodada, digite um numero:  "))
    
    if numero == aleatorio:
    
        print("Você venceu")
        break
    
print("Acabou o Jogo")