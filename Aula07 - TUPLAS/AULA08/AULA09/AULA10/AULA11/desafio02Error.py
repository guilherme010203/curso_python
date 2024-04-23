try:
    with open("dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("o arquivo nao existe")