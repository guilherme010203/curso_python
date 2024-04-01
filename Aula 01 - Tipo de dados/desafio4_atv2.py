frase = input("digite uma frase").upper()


contaCaracter = frase.count("A")
inicioCaracter = frase.find("A")
ultimoCaracter = frase.rfind("A")


#identificando quantas vezes aparece uma caracter especifica
print(f"a letra A apareceu {contaCaracter} vezes")


#indentificando onde ela aparece pela primeira vez
print(f"a letra A apareceu pela primiera vez na {inicioCaracter} posiçao")

#identificando onde ela aparece pela ultima vez
print(f"a letra A apareceu pela ultima vez na {ultimoCaracter} posiçao")