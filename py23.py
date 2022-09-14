import math
ang = float(input('Angulo :'))
ang = math.radians(ang)
sen = math.sin(ang)
cos = math.cos(ang)
tg = math.tan(ang)
print('Dados(\nAngulo em radianos:{:.1f}\nvalor da seno:{:.1f}\ncosseno:{:.1f}\ntangente:{:.1f}\n)'.format(ang,sen,cos,tg))