palavra = input()
alfabeto = 'abcdefghijklmnopqrstuvxz'
vogais = 'aeiou'
if palavra.islower() == True and 1 <= len(palavra) <= 30:
    nova = palavra[0]
    for x in range(0,len(palavra)):
        for y in range(0,len(alfabeto)):
            if alfabeto.index(palavra[x]) 

