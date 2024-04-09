
def contar_nove(tupla):
    return tupla.count(9)


def posicao_tres(tupla):
    if 3 in tupla:
        return tupla.index(3) + 1  


def numeros_pares(tupla):
    return [num for num in tupla if num % 2 == 0]


def main():
   
    valores = tuple(map(int, input("Digite quatro valores separados por espaço: ").split()))

    vezes_nove = contar_nove(valores)
    print("A) O valor 9 apareceu", vezes_nove, "vezes.")

   
    posicao = posicao_tres(valores)
    if posicao:
        print("B) O primeiro valor 3 foi digitado na posição", posicao)
    else:
        print("B) O valor 3 não foi digitado.")

    
    pares = numeros_pares(valores)
    if pares:
        print("C) Os números pares digitados foram:", pares)
    else:
        print("C) Não foram digitados números pares.")

if __name__ == "__main__":
    main()

  