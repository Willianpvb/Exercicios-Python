game = True
while game:
    n = int(input('número de participantes:'))
    if 1000 >= n >= 1:
        pequeno = 0
        medio = 0
        for x in range(0, n):
            a = int(input('tamanho escolhido 1(pequeno) ou 2(medio):'))
            if a == 1:
                pequeno += 1
            elif a == 2:
                medio += 1
            else:
                print()

        p = int(input('quantidade de camisas pequenas produzidas:'))
        m = int(input('quant. de camisas medias produzidas:'))
        if p > 1000 or m > 1000:
            print('falha')
        if p == pequeno and m == medio:
            print("S")
            game = False
        else:
            print("N")
            game = False
    else:
        print("ERRO")
