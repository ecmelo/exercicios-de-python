from datetime import date

anoAtual = date.today().year
idade = maioridade = menoridade = 0
for c in range (1, 8):
    anoNascimento = int(input(f'Em que ano a {c}ª pessoa nasceu: '))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        maioridade += 1
    elif idade < 21:
        menoridade += 1

print(f'O numero de pessoas maiores de idade é {maioridade} e o número de pessoas menores de idade é {menoridade}')