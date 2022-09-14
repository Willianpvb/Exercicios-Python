aluno = dict()

aluno['nome'] = input('Nome:')

nota1 = float(input('nota 1:'))
nota2 = float(input('nota 2:'))
aluno['media'] = (nota1 + nota2)/2

if aluno['media'] <= 4:
    aluno['situação'] = "reprovado"
elif aluno['media'] < 7:
    aluno['situação'] = "em recuperação"
else:
    aluno['situação'] = 'Aprovado'

print('=-'*20)
for keys, values in aluno.items():
    print(f'- {keys} é igual a {values}')

print('=-' * 20)

print(f'O Aluno: {aluno["nome"]}.\nCom a media {aluno["media"]}.'
      f'\nAtualmente ele está {aluno["situação"]}.')
print('=-'*20)

print(aluno)