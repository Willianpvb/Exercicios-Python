irmas = []
for x in range(0, 3):
    idade = int(input())
    if 5 <= idade <= 100:
        irmas.append(idade)
irmas.sort()
print(irmas[1])