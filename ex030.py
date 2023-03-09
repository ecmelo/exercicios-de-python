n = int(input('Digite um número: '))

resto = n%2
if resto == 0:
    print('O numero {} é par!'.format(n))
else:
    print('O numero {} é impar!'.format(n))