num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 == num2:
    print('os dois números tem o mesmo valor!')
elif num1 < num2:
    print(f'o segundo número digitado {num2} é maior que o primeiro número digitado {num1}')
elif num1 > num2:
    print(f'o primeiro número digitado {num1} é maior que o segundo número digitado {num2}')