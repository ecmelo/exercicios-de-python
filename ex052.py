n = int(input('Digite um número: '))
tot = 0
for c in range (1, n+1):
    if n % c == 0:
        tot += 1
print(f'O número {n} foi dividido {tot} vezes', end=' ')
if tot > 2:
    print('não é PRIMO')
else:
    print('é PRIMO')

