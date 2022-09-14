viagem = int(input("Qual a distância da viagem em KM:"))
if viagem <= 200:
    print("{}$ é o valor total da passagem de até 200 KM.".format(viagem*0.5))
else:
    print("{}$ valor de passagem além de 200Km de distância.".format(viagem*0.45))