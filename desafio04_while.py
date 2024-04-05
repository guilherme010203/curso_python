import random

vitorias_consecutivas = 0

while True:
    jogador = input("Escolha par (P) ou ímpar (I): ").upper()
    if jogador not in ['P', 'I']:
        print("Escolha inválida. Por favor, escolha P para par ou I para ímpar.")
        continue
    
    jogador_numero1 = int(input("Escolha um número entre 0 e 10: "))
    if jogador_numero1 < 0 or jogador_numero1 > 10:
        print("Número inválido. Por favor, escolha um número entre 0 e 10.")
        continue
    
    computador_numero = random.randint(0, 10)
    print("O computador escolheu:", computador_numero)
    
    total = jogador_numero1 + computador_numero
    
    if (jogador == 'P' and total % 2 == 0) or (jogador == 'I' and total % 2 != 0):
        print("Você ganhou!")
        vitorias_consecutivas += 1
    else:
        print("Você perdeu!")
        break

print("Total de vitórias consecutivas:", vitorias_consecutivas)