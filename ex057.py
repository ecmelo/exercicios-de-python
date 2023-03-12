while True:
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F':
        print(f'Sexo [{sexo}] feminino registrado com sucesso!')
        break
    elif sexo == 'M':
        print(f'Sexo [{sexo}] masculino registrado com sucesso!')
        break
    else:
        print('Sexo inválido, tente novamente.')