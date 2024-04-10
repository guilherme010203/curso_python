import random

class Roleta:
    def __init__(self):
        self.numeros = list(range(0, 37))  # Números de 0 a 36 na roleta
        self.cor_vermelha = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.cor_preto = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.cor_verde = [0]  # O zero é verde
        self.ultimos_resultados = []

    def girar(self):
        numero_sorteado = random.choice(self.numeros)
        self.ultimos_resultados.append(numero_sorteado)
        return numero_sorteado

    def verificar_cor(self, numero):
        if numero in self.cor_vermelha:
            return 'vermelho'
        elif numero in self.cor_preto:
            return 'preto'
        elif numero in self.cor_verde:
            return 'verde'
        else:
            return 'desconhecido'

    def mostrar_ultimos_resultados(self, quantidade=5):
        print("Últimos resultados da roleta:")
        for resultado in self.ultimos_resultados[-quantidade:]:
            print(resultado)

# Exemplo de uso
roleta = Roleta()

# Girar a roleta
resultado = roleta.girar()
print("Número sorteado:", resultado)
print("Cor:", roleta.verificar_cor(resultado))

# Mostrar últimos resultados
roleta.mostrar_ultimos_resultados()
