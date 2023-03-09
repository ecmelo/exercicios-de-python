from datetime import date

anoAtual = date.today().year
nascimento = int(input('Digite o seu ano de nascimento: '))

idade = anoAtual - nascimento

if idade <= 8:
    print('CATEGORIA: Mirim')
elif idade <= 14:
    print('CATEGORIA: Infantil')
elif idade <= 19: 
    print('CATEGORIA: Júnior')
elif idade <= 20: 
    print('CATEGORIA: Senior')
elif idade > 20: 
    print('CATEGORIA: Master')