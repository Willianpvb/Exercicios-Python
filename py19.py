from math import sqrt
co = float(input("Cateto Oposto:"))
ca = float(input("Cateto Adjacente:"))
hipotenusa = sqrt((co*co)+(ca*ca))
print("Comprimento Da hipotenusa:{:.2f}".format(hipotenusa))
