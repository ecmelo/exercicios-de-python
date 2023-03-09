nome = str(input('Digite seu nome completo: ')).strip()

nomeMaius = nome.upper()
nomeMinus = nome.lower()
tamNome = len(nome)-nome.count(' ')
dividido = nome.split()
primeiroNome = len(dividido[0])


print('{} em Maiusculo fica {}, em Minusculo fica {}, tem ao todo {} letras e o primeiro nome tem {} letras'.format(nome, nomeMaius,nomeMinus, tamNome, primeiroNome))