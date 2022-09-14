print("""lista = []
for i in range(0,10):
    n = int(input())
    if 0 < n < 10000:
        lista.append(n)
cont = int(input())
print(lista.count(cont))""")

sexo = []
salarios = []

for i in range(0,10):
    salario = int(input())
    sex = input()
    sexo.append(sex)
    salarios.append(salario)

homens = sexo.count('m')
mulheres = sexo.count('f')
medias = sum(salarios) / len(salarios)
maiors = 0
mediaH = []

for i in range(0,len(salarios)):
    if maiors < salarios[i]:
        maiors = salarios[i]

maiors = sexo[salarios.index(maiors)]

for i in range(0,len(sexo)):
    if sexo[i] == "m":
        mediaH.append(salarios[i])

mediaH = sum(mediaH) / len(mediaH)

print(homens)
print(mulheres)
print('{:.2f}'.format(medias))
print(maiors)
print('{:.1f}'.format(mediaH))