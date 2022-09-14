# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Qual o valor do seu salário:'))
if salario <= 1250:
    salario = salario * 1.15
else:
    salario = salario * 1.1
print("Salario Ajustado ",salario)
