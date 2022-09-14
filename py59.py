nums = ('Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',11,12,13,14,15,16,17,18,19,20)
while True:
    escolha = int(input('Escolha um número inteiro de 1 à 20:'))
    if 1 <= escolha <= 20:
        print(f'Vc escolheu {nums[escolha - 1]}')
        break




