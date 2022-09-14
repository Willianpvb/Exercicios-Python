carro = int(input("Qual é a velocidade do seu carro? "))
if carro <= 80:
    print("Muito Bem")
else:
    print("Foi multado doidin, a multa é de {} reais".format((carro-80)*7))