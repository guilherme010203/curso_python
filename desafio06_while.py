total_gasto = 0
produtos_mais_de_100 = 0
nome_produto_mais_barato = None
preco_produto_mais_barato = float('inf')  # Inicializa com um valor muito alto

while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$ "))
    
    total_gasto += preco_produto
    
    if preco_produto > 100:
        produtos_mais_de_100 += 1
    
    if preco_produto < preco_produto_mais_barato:
        nome_produto_mais_barato = nome_produto
        preco_produto_mais_barato = preco_produto
    
    continuar = input("Deseja adicionar mais produtos? (s/n): ").lower()
    if continuar != 's':
        break

print("\nTotal gasto na compra: R$ {:.2f}".format(total_gasto))
print("Quantidade de produtos custando mais de R$ 100,00:", produtos_mais_de_100)
print("Nome do produto mais barato:", nome_produto_mais_barato)