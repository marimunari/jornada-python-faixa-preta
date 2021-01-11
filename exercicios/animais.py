animais = []

animal = input('Digite o nome de seus animais ou digite 0 se não tiver nenhum: ')

while animal != '0':
    especie = input('Digite a espécie desse animal: ')
    animais.append([animal, especie])
    animal = input('Se tiver mais animais, digite o nome dele, caso contrário, digite 0.')

if len(animais) == 0:
    print('\n\nVocê não tem animais')
else:
    for animal in animais:
        print('- Nome:', animal[0], ' | Espécie:', animal[1])