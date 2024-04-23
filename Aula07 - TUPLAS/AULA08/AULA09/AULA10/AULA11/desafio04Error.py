try:
    nome = input("digite o seu nome:   ")
    idade = int(input("digite sua idade:   "))
except ValueError:
    print("DIGITE SUA IDADE COM VALOR NUMERICO")    

else:
    print(f"CADASTRO CONCLUIDO")    