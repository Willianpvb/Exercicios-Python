lista = []
continuar = True
cont = 0
while continuar:
    valor = int(input(f"digite o valor {cont}: "))
    cont += 1
    if valor not in lista:
        lista.append(valor)
    else:
        print("Valor já existente...Então não será adicionado.")
    teste = input("Quer continuar?(S/N)")
    if teste == "N" or teste == "n":
        continuar = False
print("XXXX"*len(lista))
print(lista)