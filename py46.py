# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
def ex36():
    casa = float(input("Qual o valor da casa?"))
    salario = float(input("Qual é seu salário?"))
    meses = (int(input("Em quantos anos pretende pagar?")))*12
    prestacoes = casa / meses
    if prestacoes >= (salario * 0.3):
        print('Emprestimo não concedido')
    else:
        print('Emprestimo concedido')


ex36()
