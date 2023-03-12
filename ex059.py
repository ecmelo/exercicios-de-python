num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
opção = 0

while opção != 5:
    print(''' O que você deseja fazer? 
    [1] Somar 
    [2] Multiplicar
    [3] Maior número
    [4] Novos números
    [5] Sair do programa
    ''')
    opção = int(input('Digite uma opção: '))
    if opção == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    elif opção == 2:
        multiplicação = num1 * num2
        print(f'{num1} x {num2} = {multiplicação}')
    elif opção == 3:
        if num1 > num2:
            maior = num1
            print(f'Entre {num1} e {num2} maior é o {maior}')
        elif num2 > num1:
            maior = num2
            print(f'Entre {num1} e {num2} maior é o {maior}')
        else:
            print('Os dois números são iguais')
    elif opção == 4:
        print('Escolha novos números')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    elif opção == 5:
        print('Finalizando...')
    else: 
        print('Opção inválida, tente novamente.')
print('Fim.')