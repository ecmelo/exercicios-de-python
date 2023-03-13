n = int(input('Quantos termos você quer mostrar? '))
primeiroTermo = 0
seguntoTermo = 1
print(f'{primeiroTermo} -> {seguntoTermo}', end='')
cont = 3
while cont <= n:
    seguinte = primeiroTermo + seguntoTermo
    print(f' -> {seguinte}', end='')
    primeiroTermo = seguntoTermo
    seguntoTermo = seguinte
    cont += 1
        
print(' -> Fim')