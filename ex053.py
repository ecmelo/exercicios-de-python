frase = str(input('Digite aqui: ')).strip().upper()
palavras = frase.split()
juntando = ''.join(palavras)
inversao = ''
for letra in range (len(juntando) - 1, -1, -1):
    inversao += juntando[letra]
if inversao == juntando:
    print(f'Temos um palindromo!')
else:
    print(f'A frase não é um palindromo')
    
print(frase)
print(juntando, inversao)