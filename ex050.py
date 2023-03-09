j = soma = 0
for c in range (0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        j += 1
        soma += n
print(f'A quantidade de números pares são: {j} e a sua soma foi {soma}')