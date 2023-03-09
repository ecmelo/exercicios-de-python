cidade = str(input('Digite o nome da sua cidade: '))
cidadeComeca = cidade.split()
existeSanto = 'Santo' in cidadeComeca[0]

if existeSanto == True:
    print('Sua cidade começa com a palavra Santo')
else:
    print('Sua cidade não começa com a palavra Santo')