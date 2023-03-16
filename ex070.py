soma = acima1000 = maisCaro = maisBarato = j = 0
nomeBarato = nomeCaro = ''
while True:
    produto = str(input('Nome do produto: '))
    valor = int(input('Valor do produto: '))
    soma += valor
    j += 1
    resposta = ' '
    if valor >= 1000:
       acima1000 += 1  
    if j == 1:
        maisCaro = valor
        maisBarato = valor
    else:
        if valor > maisCaro:
            maisCaro = valor
            nomeCaro = produto
        if valor < maisBarato:
            maisBarato = valor
            nomeBarato = produto
    while resposta not in 'SN':
        resposta = str(input('Gostaria de inserir mais produtos? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'O total da compra ficou em: R$ {soma}')
print(f'A quantidade de produtos acima de R$ 1000.00 são R$ {acima1000}')
print(f'O produto mais caro é {nomeCaro} custando R$ {maisCaro:.2f}', end=' ')
print(f'e o mais barato é {nomeBarato} custando R$ {maisBarato:.2f}')