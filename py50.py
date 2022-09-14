matriz = []
# Tamanho da matrizz quadrada:
tam = int(input())

# add valores no formato numrero+espaço+numero => '4 5'
for x in range(tam):
    l = input()
    l = l.strip()
    linha = l.split(' ')
    for z in range(len(linha)):
        linha[z] = int(linha[z])
    matriz.append(linha[0:tam])
# contar valor total das linhas pares e impares
pares = 0
impares = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i % 2 == 0:
            pares += matriz[i][j]
        else:
            impares += matriz[j][i]

# calcular diagonal principal
diagonal = 0
for x in range(len(matriz)):
    diagonal += matriz[x][x]

# Cases
maior = diagonal
for i in range(3):
    if maior < impares:
        maior = impares
    elif maior < pares:
        maior = pares
if maior == impares & maior == pares:
    print("Empate!\nResultado:", maior)
elif maior == diagonal:
    print("O intrometido venceu!\nResultado:", maior)
elif maior == impares:
    print("A entidade venceu!\nResultado:", maior)
elif maior == pares:
    print("Arthur venceu!\nResultado:", maior)
