import math

ang = float(input('Digite um ângulo: '))


sen = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))
cose = math.cos(math.radians(ang))

print('Os respectivos seno {:.2f}, coseno{:.2f} e tangente {:.2f} do angulo digitado {}'.format(sen, cose, tang, ang))