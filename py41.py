n = int(input())
for x in range(0, n):
    l1 = input().split()
    p1 = l1[0]
    p2 = l1[1]
    p = ''

    if len(p1) < len(p2):
        menor = len(p1)
        for x in range(0, menor):
            p += p1[x] + p2[x]
        p += p2[menor:]
    else:
        menor = len(p2)
        for x in range(0, menor):
            p += p1[x] + p2[x]
        p += p1[menor:]
    print(p)

cont = 0
qtd = int(input())

while cont < qtd:
    linha = input().split()
    palavra_1 = linha[0]
    palavra_2 = linha[1]
    final_palavra = ""
    cont2 = 0

    while cont2 < len(palavra_1) and cont2 < len(palavra_2):
        final_palavra += palavra_1[cont2] + palavra_2[cont2]
        cont2 += 1

    if cont2 < len(palavra_1):
        final_palavra += palavra_1[cont2:]

    if cont2 < len(palavra_2):
        final_palavra += palavra_2[cont2:]

    print(final_palavra)
    cont += 1