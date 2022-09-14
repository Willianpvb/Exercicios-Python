lista = []
for x in range(5):
    valor = int(input(f"digite o valor: "))
    lista.append(valor)
    l2 = lista[:]
    for y in range(len(lista)):
        if len(lista) <= 1:
            print("Primeiro Valor Adicionado...")
        else:
            if min(lista) == valor:
                lista[0] = valor

def adiantar(lista):


print(lista)