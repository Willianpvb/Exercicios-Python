lanche = ('Pzza', 'Pudim', 'Suco') #TUPLA
lanche = 'Pzza', 'Pudim', 'Suco' #TUPLA
print(lanche[-3])
print(f'Tupla: {lanche}')
for posicao, comida in enumerate(lanche):
    print(f'lanche: {comida}, na posição {posicao}')

print(sorted(lanche))