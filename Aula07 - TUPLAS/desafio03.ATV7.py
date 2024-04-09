clasificaçao = 'Operário Ferroviário EC PR','CR Brasil AL','Grêmio Novorizontino SP','Ituano FC SP','Ponte Preta','Guarani FC SP','Ceará SC CE','Botafogo FC SP','Paysandu SC PA','Amazonas FC AM','Goiás EC GO','Mirassol FC','Chapecoense','Vila Nova GO','Coritiba PR','América FC MG','Avaí FC SC','Recife','Brusque','Santos FC SP',
# A) Apenas os 5 primeiros colocados
print("A) Os 5 primeiros colocados:")
print(clasificaçao[:5])

# B) Os últimos 4 colocados da tabela
print("\nB) Os últimos 4 colocados da tabela:")
print(clasificaçao[-4:])

# C) Uma lista com os times em ordem alfabética
print("\nC) Times em ordem alfabética:")
print(sorted(clasificaçao))

# D) Em que posição na tabela está o time do Santos
time_santos = "Time Santos"
posicao_santos = clasificaçao.index(time_santos) + 1  # Adiciona 1 porque a indexação começa em 0
print(f"\nD) O time do Santos está na posição {posicao_santos} na tabela.")

