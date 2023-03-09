compras = int(input('Digite o valor gasto na loja: '))
print("""
[1] À vista Dinheiro/Cheque: desconto de 10%
[2] À vista no cartão: desconto de 5%
[3] Em até duas vezes no cartão: preço normal 
[4] 3x ou mais no cartão: Juros de 20%""")
opçaoPagamento = int(input('Escolha a forma de pagamento: '))
valorFinal = 0
if opçaoPagamento == 1:
    valorFinal = compras - (compras*10)/100
    print(f'O valor final com desconto ficou de: {valorFinal}')
elif opçaoPagamento == 2:
    valorFinal = compras - (compras*5)/100
    print(f'O valor final com desconto ficou de: {valorFinal}')
elif opçaoPagamento == 3:
    print(f'O valor final é o valor normal gasto, de: {compras}')
elif opçaoPagamento == 4:
    parcelas = int(input('Quantas parcelas:'))
    valorFinal = compras + (compras * 20)/100
    parcelasVezes = valorFinal / parcelas
    print(f'O valor final ficou em: {valorFinal}, cada parcela ficou em: {parcelasVezes}')