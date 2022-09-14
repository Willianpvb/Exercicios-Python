n = int(input("Possivel Número Primo:"))
cont = 0
for c in range(n,0,-1):
    if n % c == 0:
        print("\033[1:42m",end=" ")
        cont+=1
    else:
        print("\033[1:41m",end=" ")
    print(c,end=" ")

print("\033[m")

if cont > 2:
    print("\033[4m{} Não é PRIMO\033[m".format(n))
else:
    print("\033[4m{} é PRIMO\033[m".format(n))
