frase = str(input('Digite uma frase: ')).lower().strip()
frase1 = frase.count('a')
posicaoFrase = frase.find('a')
ultimaPosicaoFrase = frase.rfind('a')
print('A quantidade de vezes que aparece a palavra "A" na frase é {}'.format(frase1))
print('A primeira vez que aparece a letra "A" é na posição {}'.format(posicaoFrase))
print('A última vez que aparece a letra "A" é na posição {}'.format(ultimaPosicaoFrase))