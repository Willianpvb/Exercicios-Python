n = int(input())
rec = []
env = []
temp = []
if 1 <= n <= 10:
    for x in range(0, n):
        num = input().split()
        if 1 <= int(num[1]) <= 100:
            if num[0] == 'R':
                rec.append(num[1])
                temp.append([num[1], 0])
            elif num[0] == 'E':
                env.append(num[1])
                temp.append([num[1], 0])
            if num[0] == 'T':
                temp.append([rec[len(rec)-1], num])
            else:
                temp.append([rec[len(rec)-1], 1])

for y in rec:
    for z in env:
        if y == z:
            soma = 0
            for yz in temp:
                if z == yz[0]:
                    soma += int(yz[1])
            print(y,soma)
            print(z, soma)
