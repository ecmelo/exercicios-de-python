mais18 = homens = mulhermenos20 = j= 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1    
    if sexo == 'F' and idade < 20:    
        mulhermenos20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'Tem {mais18} pessoas com mais de 18 anos.')
print(f'São {homens} homens.')
print(f'Tem {mulhermenos20} mulheres com menos de 20 anos.')
print(j)