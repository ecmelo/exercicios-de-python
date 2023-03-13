n = int(input('Digite um número para saber seu fatorial: '))
c = n
fatorial = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(fatorial)