from datetime import time
import datetime

ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))


if ano == 0:
    ano = datetime.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é ano BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))