from datetime import date

anoAtual = date.today().year
nascimento = int(input('Digite o ano em que você nasceu: '))
idade = anoAtual - nascimento
saldo = 0

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não pode se alistar, faltam: {saldo} anos para o seu alistamento!')
    print(f'Você vai se alistar em: {anoAtual + saldo}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos atás!')
    print(f'Você deveria ter se alistado em {anoAtual - saldo}')