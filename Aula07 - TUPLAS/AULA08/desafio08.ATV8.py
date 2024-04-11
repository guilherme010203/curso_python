matriz= [[0,0,0],[1,1,1],[2,2,2]]
c=0

for i in range (0,3):
   
    for j in matriz[i]:
       
        if c==3:
            c=0
                 
        numero= int(input(f"Digite um valor para[{i},{c}]: "))
       
        matriz[i][c]=numero    
        c +=1
       
# print(matriz)
print(matriz[0])
print(matriz[1])
print(matriz[2])

# Função para imprimir a matriz com a formatação correta
def imprimir_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f"{valor:8.2f}", end=" ")
        print()

# Função para calcular a soma dos valores pares na matriz
def soma_valores_pares(matriz):
    soma = 0
    for linha in matriz:
        for valor in linha:
            if valor % 2 == 0:
                soma += valor
    return soma

# Função para calcular a soma dos valores da terceira coluna
def soma_terceira_coluna(matriz):
    soma = 0
    for linha in matriz:
        soma += linha[2]
    return soma

# Função para encontrar o maior valor na segunda linha
def maior_valor_segunda_linha(matriz):
    max_valor = matriz[1][0]  # Inicializa com o primeiro valor da segunda linha
    for valor in matriz[1]:
        if valor > max_valor:
            max_valor = valor
    return max_valor
print("A) Soma dos valores pares:", soma_valores_pares(matriz))
print("B) Soma dos valores da terceira coluna:", soma_terceira_coluna(matriz))
print("C) Maior valor da segunda linha:", maior_valor_segunda_linha(matriz))
