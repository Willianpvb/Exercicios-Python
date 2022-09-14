#O menor e o maior entre 3 números
mame = []
for x in range(0, 3):
    n = int(input())
    mame.append(n)
mame.sort()
print('Menor: {}\nMaior: {}'.format(mame[0], mame[2]))
