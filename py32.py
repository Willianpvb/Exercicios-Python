import random
aleatorio = random.randint(0,5)
user = int(input("Escolha e digite um número entre 0 e 5:"))
if user == aleatorio:
    print("Acertou")
else:
    print("errou")
print("Número do Computador:{}".format(aleatorio))