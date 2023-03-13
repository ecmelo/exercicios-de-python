cont = soma = 0
while True:
    n = int(input('Digite um número [Parar: 999] '))
    if n == 999:
        break
    else:
        cont += 1
        soma += n
print(f'A soma dos {cont} números deu {soma}')