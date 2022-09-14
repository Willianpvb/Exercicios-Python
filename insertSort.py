def insertSort(lista):
    for i in range(1, len(lista)):
        print('\n------Nova Comparação------\n')
        valorAtual = lista[i]
        pos = i

        print('{} > {}'.format(lista[pos - 1], valorAtual), valorAtual < lista[pos - 1])
        while pos > 0 and lista[pos - 1] > valorAtual:
            print('\nTrocar posição {} com {}'.format(lista[pos - 1], valorAtual))
            print('Lista Atual:',lista)
            lista[pos] = lista[pos - 1]
            pos -= 1
            print('Lista Parcial:', lista)
        lista[pos] = valorAtual
        print('Lista Ajustada:',lista)



def bubbleSort(lista):
    for i in range(len(lista)-1, 0 ,-1):# 7
        print('Lista Atual:', lista)
        for j in range(0,i):
            print('>',i,j)
            print(lista[j], lista[j + 1])
            if lista[j] > lista[j+1]:
                print('\nTrocar posição {} com {}'.format(lista[j], lista[j+1]))
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print('Lista Ajustada:', lista)

l = [1, 45, 75, 5, 7, 16, 53, 95]
bubbleSort(l)
print(l)


def selectionSort(lista):
    for i in range(1, len(lista)):
        print('\n------Nova Comparação------\n')
        min_idx = i

        for j in range(i + 1, len(lista)):
            print('{} > {}'.format(lista[min_idx], lista[j]), lista[j] < lista[min_idx])
            if lista[min_idx] > lista[j]:
                print('\nTrocar posição {} com {}'.format(lista[min_idx], lista[j]))
                print('Lista Atual:', lista)
                min_idx = j

        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        print('\nLista Ajustada:', lista)
