import random

t = (random.randint(0,10))
u = (random.randint(0,10))
p = (random.randint(0,10))
l = (random.randint(0,10))
a = (random.randint(0,10))
tupla = (t, u, p, l, a)

print(tupla)

menor = tupla[0]
for x in tupla:
    if menor > x:
        menor = x
print(f'Menor {menor}')

maior = tupla[0]
for y in tupla:
    if maior < y:
        maior = y
print(f'Maior {maior}')

tupla2 = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
print(tupla2)
print(max(tupla2))
print(min(tupla2))
print(sorted(tupla2))
