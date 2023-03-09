from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Sua jogada: '))

if computador == 0:
    if jogador == 0:
       print('Empate') 
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogava Inválida')
elif computador == 1:
    if jogador == 0:
        print('Computador Vence') 
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogava Inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador Vence!')
    elif jogador == 1:
        print('Computador Vence!')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogava Inválida')
print(f'Você jogou: {itens[jogador]}')
print(f'O computador jogou: {itens[computador]}')