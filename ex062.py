primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você quer? '))
print(f'Ao total foram solicitado {total} termos')
print('Fim')