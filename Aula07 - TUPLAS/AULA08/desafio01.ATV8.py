numeros = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número:  ')),int(input('Digite um número:  ')),int(input('Digite um número:  ')))
maior = (max(numeros))
menor = (min(numeros))
posicao_maior = numeros.index(maior) + 1
posicao_menor = numeros.index(menor) + 1

print(f"O menor valor foi {menor} ele se encontra na posição {posicao_menor}")
print(f"O maior valor foi {maior} ele se encontra na posição {posicao_maior}") 