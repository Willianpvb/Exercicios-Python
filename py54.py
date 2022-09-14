m = []
listamenores = []
#add lista
x = int(input())
y = int(input())
for i in range(x):
    lista = []
    for j in range(y):
        l = int(input())
        lista.append(l)
    m.append(lista)

def posicoesb(i, j):
    cima = direita = esquerda = baixo = m[i][j]
    cd = ce = bd = be = m[i][j]
    if i - 1 >= 0 and j - 1 >= 0: #cima lateral direita
        cd = m[i - 1][j - 1]

    if i - 1 >= 0 and j + 1 < y: #cima lateral esquerd
        ce = m[i - 1][j + 1]

    if i + 1 < len(m) and j + 1 < y:#BAIXO lateral direita
        bd = m[i + 1][j + 1]

    if i + 1 < len(m) and j - 1 >= 0: #baixo lateral esquerda
        be = m[i + 1][j - 1]

    if i - 1 >= 0:
        cima = m[i - 1][j]

    if j + 1 < y:
        direita = m[i][j + 1]

    if i + 1 < len(m):
        baixo = m[i + 1][j]

    if j - 1 >= 0:
        esquerda = m[i][j - 1]

    listap = [cima, baixo, direita, esquerda, cd, ce, bd, be]
    return listap


def qualemenor(posicoes):
    menorn = m[i][j]
    cont = 0
    for x in posicoes:
        if menorn == x:
            cont += 1
    if cont != 8:
        for x in posicoes:
            if menorn > x:
                menorn = x
    else:
        menorn += 1
    return menorn


for i in range(x):
    for j in range(y):
        menor = qualemenor(posicoesb(i, j))
        if menor == m[i][j]:
            listamenores.append((i, j))

print(listamenores)
