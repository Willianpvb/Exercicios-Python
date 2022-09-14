princesas = int(input())
eleitores = int(input())

# add valores
lprincesas = []
for x in range(eleitores):
    l = input()
    linha = l.strip().split(' ')
    for z in range(len(linha)):
        linha[z] = int(linha[z])
    lprincesas.append(linha[0:princesas])

for z in range(princesas):
    votos = 0
    for y in range(eleitores):
        if lprincesas[y][z] == 1:
            votos += 1
    print('Princesa {}: {} voto(s)'.format(z+1, votos))

