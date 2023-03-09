vCasa = float(input('Digite o valor da casa: '))
vSalario = float(input('Digite seu salário: '))
pagamento = int(input('Em quantos anos você pretente pagar: '))
meses = pagamento * 12
prestacao = vCasa / meses
porcento = ((vSalario * 30)/100)

if prestacao > porcento:
    print(f'Cada prestação tem o valor de {prestacao}, é 30% maior que o valor permitido em relação ao salário, empréstimo negado!')
if prestacao < porcento:
    print(f'Valor da prestação: {prestacao}, empréstimo liberado!')