n = int(input())
resultado = []
if 1 <= n <= 100000:
    for x in range(0, n):
        num = int(input())
        resultado.append(num)
    for x in resultado:
        if x == 0:
                del resultado[resultado.index(x)-1]
                del resultado[resultado.index(x)]
                print(resultado)

    print(sum(resultado))