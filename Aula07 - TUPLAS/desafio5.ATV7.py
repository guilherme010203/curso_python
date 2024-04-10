from tabulate import tabulate
lista = [['X-salada','R$21.99'],['X-burguer','R$19.99'],['X-picanha','R$20.50'],['X-bacon','R$23.99',]]
tupla = tuple(lista)

print(tabulate(tupla, headers=["produto", "preço"]))















