matriz = []
# Tamanho da matrizz quadrada:
tam = int(input())
# add valores
for x in range(tam):
    l = input()
    linha = l.strip().split(' ')
    for z in range(len(linha)):
        linha[z] = int(linha[z])
    matriz.append(linha[0:tam])

# Completar tabela
for i in range(1,len(matriz)):
    for j in range(1,len(matriz)):
        if matriz[i][j-1] + matriz[i-1][j-1] + matriz[i-1][j] >= 2:
            matriz[i][j] = 0
        else:matriz[i][j] = 1
print(matriz[tam-1][tam-1])




