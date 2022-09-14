game = True
media = (50*0.8,35*0.6,7)
testes = []
contador = 0
while game:
    n = float(input())
    if n < 0:
        game = False
    else:
        testes.append(n)
        cont = 0
        if len(testes) == 3:
            for x in range(len(media)):
                if testes[x] >= media[x]:
                    cont += 1
            testes = []
            if cont == 3:
                contador += 1
print(contador)


