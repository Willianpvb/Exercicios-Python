m = []
table = int(input())
for x in range(table):
    l = input()
    linha = l.strip().split(' ')
    for z in range(len(linha)):
        linha[z] = int(linha[z])
    m.append(linha[0:table])

somar = 0
qtd = 0
for i in range(len(m)):
    for j in range(len(m)):
        if (j + 1) < len(m):
            if m[i][j + 1] >= 0:
                somar += m[i][j + 1]
                qtd += 1

        if (j - 1) >= 0:
            if m[i][j-1] >= 0:
                somar += m[i][j-1]
                qtd += 1

        if (i + 1) < len(m):
            if m[1 + i][j] >= 0:
                somar += m[i + 1][j]
                qtd += 1

        if (i - 1) >= 0:
            if m[i - 1][j] >= 0:
                somar += m[i - 1][j]
                qtd += 1

print(qtd)
print(somar)
