from random import randint
l = []
for x in range(5):
    l.append(randint(0,1000))
print(l)
print(f"Menor {min(l)} na posição {l.index(min(l))}")
print(f"Maior {max(l)} na posição {l.index(max(l))}")