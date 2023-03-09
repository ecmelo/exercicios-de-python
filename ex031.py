distancia = int(input('Digite a distância da viagem: '))
dmenor200 = 0.5
dmaior200 = 0.45
vtotalDmenor = distancia * dmenor200
vtotalDmaior = distancia * dmaior200
if distancia <= 200:
    print(f'A distancia foi {distancia}, ficando o custo da viagem em: {vtotalDmenor}')
elif distancia > 200:
    print(f'A distancia foi {distancia}, ficando o custo da viagem em: {vtotalDmaior}')