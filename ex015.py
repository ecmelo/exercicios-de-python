aluguel = int(input('Quantos dias você alugou o carro? '))
distancia = int(input('Quantos KMs você percorreu? '))

km = 0.15
dia = 60

totalDias = aluguel * dia
totalKM = distancia * km
totalPagar = totalDias + totalKM

print('Você alugou o carro durante {} dias e percorreu {} kms, o total a pagar ficou em {}R$'.format(aluguel, distancia, totalPagar))