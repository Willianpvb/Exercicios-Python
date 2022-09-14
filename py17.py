km = float(input("Quantidade de Km rodados:"))
dias = int(input("Dias alugados:"))
preco = km*0.15 + dias*60
print("Total a pagar por dias e km rodados:{:.2f}".format(preco))