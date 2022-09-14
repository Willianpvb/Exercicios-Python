num = int(input("Choice a number from 0 to 9999:"))
n  = str(num)
numeros = []
for i in range(0,len(n)):
    if(n[i] == "" ):
        numeros.append(0)
    else:
        numeros.append(n[i])


unidade = num // 1000 % 10
dezena = num // 100 % 10
centena = num // 10 % 10
milhar = num // 1 % 10
print('Milhar: {} \nCentenas: {} \nDezenas: {} \nUnidades: {}'.format(unidade,dezena,centena,milhar))
print('Milhar: {} \nCentenas: {} \nDezenas: {} \nUnidades: {}'.format(numeros[0],numeros[1],numeros[2],numeros[3]))