pares = []
impares = []
entrada = int(input())
for x in range(0,entrada):
    nums = int(input())
    if nums % 2 == 0:
        pares.append(nums)
    else:
        impares.append(nums)
pares.sort()
impares.sort()
impares.reverse()
for y in pares:
    print(y)
for z in impares:
    print(z)

