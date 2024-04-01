frase = "Microsoft Power BI"

#trocando uma palavra
trocaPalvra = frase.replace("Power BI" , " AZ-900")
print(trocaPalvra)

#coverter todas as letras para maiuscula
print(frase.upper())


#coverter palavras para minusculo
print(frase.lower())

#coverter a primeira letra da frase
print(frase.capitalize())

#coverter a primeira letra de cada palvra de frase
print(frase.title())

cursoEspacado = "fundamentos              da                     ciencia            de dados - Google Clound"
curso = cursoEspacado.strip()
curso = cursoEspacado.rstrip()
curso = cursoEspacado.lstrip()

#removendo espaços inadequados
print(curso)