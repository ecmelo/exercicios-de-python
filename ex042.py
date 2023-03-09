reta1 = float(input('Digite o primeiro segmento: '))
reta2 = float(input('Digite o segundo segmento: '))
reta3 = float(input('Digite o terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas acima podem formar um triangulo', end=' ')
    if reta1 == reta2 == reta3:
        print('Equilétero!')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Isósceles!')
    elif reta1 != reta2 and reta1 != reta3 and reta3 != reta2:
        print('Escaleno!')
else:
    print('As retas não formam um triangulo') 