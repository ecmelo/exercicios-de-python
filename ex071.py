cedula = 200
total = 0
valor = int(input('Qual valor você gostaria de sacar: R$ '))
valorF = valor
while True:
    if valorF >= cedula:
        valorF -= cedula
        total += 1
    else:
        if total > 0:
            print(f'O total de cédulas {total} de R${cedula} ')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        total = 0
        if valorF == 0:
            break