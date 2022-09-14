ano = int(input("Que ano quer analisar?"))
print("{} é um ano bissexto".format(ano) if ano % 4 == 0 else "{} Não é ano bissexto".format(ano))

from datetime import date
if date.today().year % 4 == 0:
    print("Bissexto")
else:
    print("Não bissexto")
