import random
tentativas = 1
num = random.randint(1, 10)
while True:
    n = int(input('Digite um número: '))
    if n >= 11 or n <= 0:
        print('Número inválido, tente novamente! ')
    else: 
        if n < num:
            print('Mais... tente mais uma vez: ')
            tentativas += 1
        elif n > num:
            print('Menos... tente mais uma vez: ')
            tentativas += 1 
        else:
            break
print(f'Você acertou! Foram feitas {tentativas} tentativas até acertar.')