import math

catAdj = float(input('Digite o cateto adjacente: '))
catOp = float(input('Digite o cateto oposto: '))

hip = math.hypot(catAdj, catOp)

print('O cateto adjacente é {}, o cateto oposto é {} e a hipotenusa é {:.2f}!'.format(catAdj, catOp, hip))