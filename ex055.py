menorPeso = maiorPeso = 0
for pessoa in range (1, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
       menorPeso = peso
       maiorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print(f'Menor peso: {menorPeso}; Maior peso: {maiorPeso}')