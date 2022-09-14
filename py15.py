salario = float(input("Digite seu salario para reajuste: R$"))
nsalario = salario + (salario*15/100)
print("Seu novo salario será equivalente à:${:.2f} e o valor do aumento: {:.2f}".format(nsalario,(salario*0.15)))