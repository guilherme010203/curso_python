try:
    with open("data.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("o arquivo nao existe")        