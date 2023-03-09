salario = float(input('Digite o seu salário: '))
aumento1 = salario + (salario * 15) / 100
aumento2 = salario + (salario * 10) / 100
limite = 1250

if salario <= limite:
    print(f'O funcionário recebeu um aumento de 15%, recebe agora o salário de: {aumento1}')
elif salario > limite:
    print(f'O funcionário recebeu um aumento de 10%, recebe agora o salário de: {aumento2}')