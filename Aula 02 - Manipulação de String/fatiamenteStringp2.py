frase = "curso de python"
nome= "Guilherme Nascimento Monteiro"

#analisar o tamanho da frase 
print(len(frase))

#contar o numero de caracteres do nome 
print(len(nome))

#conta quantas vezes um caracter especifico aparece 
print(frase.count("o"))

#contando quantoas vezes um caracter especifico aparece no meu nome 
print(nome.count("e"))

#indica a posiçao de inicio uma frase desejada

print(frase.find("curso de python"))

#indica a posicao de inicio do meu sobrenome
print(nome.find("Nascimento"))

#verificando se possui a palavra frase
print("python" in frase)

#verfificando se possui a palavra nome
print("souza" in nome)

#verficiacao de dados do nome do cliente 
print("eduardo" in nome)

#verficando se possui palvra nome
print("Guilherme" in nome)
