var = input('Digite um valor: ')
print('É um alpha númerico ?', var.isalnum())
print("É um número? {}".format(var.isnumeric()))
print('está Capitalizada? {}'.format(var.istitle()))
print('é hexadecimal? ',var.isascii())
print('Tem espaços: ',var.isspace())
print('Está maiuscula:',var.isupper())
print('Está minusculo? ', var.islower())
print('É alfabetico?',var.isalpha())
print("    reE te     ".strip().title())