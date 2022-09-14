'''n = float(input('Quanto vc tem em reais?'))
dolar = n//3.27
print('Voce pode compar {} dolar(es)'.format(dolar))
n2 = str(n)
n2.count('(')

print(n2,n2.count('('))'''
n = input()
if n.count("(") == n.count(")"):
    print("correct")
else:
    print("incorect")

    n.rfind()
