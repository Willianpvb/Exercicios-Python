from time import sleep

# for i in range(10, -1, -1):
# sleep(1)
#  print(i)
# print("Felizz ano novo")
#cont = 0
#for x in range(0, 51, 2):
 #   cont += 1
  #  print(x, end=' ')
#print(cont)
cont = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        cont += x
        print(x)
print(cont)
