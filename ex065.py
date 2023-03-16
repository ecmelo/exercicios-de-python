
continuar = 'S'
j = soma = media = maiorN = menorN = 0
while continuar in 'S':
    n = int(input('Digite um número: '))
    continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    soma += n
    j += 1
    if j == 1:
        maiorN = n
        menorN = n
    else:
        if n > maiorN:
            maiorN = n
        if n < maiorN:
            menorN = n
media = soma/j
print(f'Você digitou {j} números e a mádia foi {media}')
print(f'O maior número é {maiorN} e o menor número é {menorN}')