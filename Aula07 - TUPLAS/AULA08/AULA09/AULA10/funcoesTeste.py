def calculaArea(largura, altura):
    area = largura * altura
    print(area)
    
def calculaPerimetro(largura, altura):
    perimetro = (2 * largura) + (2 * altura)
    return perimetro

largura = int(input("digite a largura:  "))
altura = int(input("digite a altura:  "))


print(calculaPerimetro(5,3))   
calculaArea(largura,altura)



