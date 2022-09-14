import random
alunos = []
for i in range(0,4):
    n = input("Qual o nome do aluno:")
    alunos.append(n.capitalize())
y = random.randint(0,3)
print("{} você foi o sorteado de hoje! Limpe o Quadro!".format(alunos[y]))
print("{} você foi o sorteado de hoje! Limpe o Quadro!".format(random.choice(alunos)))