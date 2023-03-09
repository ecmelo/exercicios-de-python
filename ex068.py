import random

maquina = j = soma = 0

while True:
    n = int(input('Diga um valor: '))
    jogo = str(input('Par ou Impar? [P/I]')).upper()
    maquina = random.randint(0, 10)
    soma = maquina + n
    if jogo == 'P' and soma % 2 == 0:
        print(f'Você jogou {n}, a maquina jogou {maquina}. Total deu {soma}, deu PAR, você venceu!')
        j += 1
    elif jogo == 'I' and soma % 2 == 1:
        print(f'Você jogou {n}, a maquina jogou {maquina}. Total deu {soma}, deu IMPAR, você venceu!')
        j += 1
    elif jogo == 'I' and soma % 2 == 0:
        print(f'Você jogou {n}, a maquina jogou {maquina}. Total deu {soma}, deu PAR, você perdeu!')
        break
    elif jogo == 'P' and soma % 2 == 1:
        print(f'Você jogou {n}, a maquina jogou {maquina}. Total deu {soma}, deu IMPAR, você perdeu!')
        break
print(f'Você ganhou {j} vezes.')