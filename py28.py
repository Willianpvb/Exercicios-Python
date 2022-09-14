nome = str(input('Qual é seu nome:')).title().strip()
print("Seu nome contém 'Silva':",nome.__contains__('Silva'),'\nObs:Mesmo efeito; desse jeito é melhor >>>', 'Silva' in nome)
