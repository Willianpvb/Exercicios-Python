letras = ('a', 'e', 'i', 'o', 'u')
palavras = (input('Digite uma palavra:'),
            input('Digite uma palavra:'),
            input('Digite uma palavra:'),
            )

for palavra in palavras:
    print(f'{palavra} possui essas vogais :')

    for vogal in letras:
        if vogal in palavra:
            print(f'-{vogal}', end='')
    print()