multiplicador = 0
n = 1
while n > 0: 
    n = int(input('Digite um número para tabuada: '))
    if n < 0:
        print('Número Inválido.')
        break
    else:
        for c in range (1, 11):
            multiplicador = n * c
            print(f'{n} x {c} = {multiplicador}')