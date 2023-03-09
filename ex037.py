n = int(input('Digite um valor: '))

print('[1] BINÁRIO', end=' ') 
print('[2] OCTADECIMAL', end=' ')
print('[3] HEXADECIMAL')
binario = bin(n)
hexa = hex(n)
octa = oct(n)


opcao = int(input('Digite a conversão desejada: '))

if opcao == 1:
    print(f'O número {n} na conversão binária ficou: {binario[2:]}')
elif opcao == 2:
    print(f'O número {n} na converção octadecimal ficou: {octa[2:]}')
elif opcao == 3:
    print(f'O número {n} na conversão hexadecimal ficou: {hexa[2:]}')
else:
    print('Opção inválida!')