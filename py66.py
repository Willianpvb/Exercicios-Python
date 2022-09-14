from random import randint
from operator import itemgetter
from time import sleep

jogadas = dict()
for i in range(1,5):
    jogadas[f'j{i}'] = randint(1,6)
print(jogadas)
rank = dict()
rank = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for x,y in enumerate(rank):
    print(f'O jogador {y[0]} tirou {y[1]}, Na posição {x+1}')
    sleep(2)

