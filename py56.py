n = int(input("Razão: "))
m = int(input("Primero termo: "))
for i in range(0, 10):
    print("{} - ".format(m + (n * i)), end="")
print("Acabou")

for i in range(m, m + n * 10, n):
    print("{} - ".format(i), end="")
print("Acabou")
