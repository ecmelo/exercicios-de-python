import random

n = int(input('Digite um número: '))

num = random.randint(0, 5)
if n == num:
	print('Você acertou!')
else: 
	print('Você errou! O número correto era: {}'.format(num))