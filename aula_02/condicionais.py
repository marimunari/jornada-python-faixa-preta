## É igual
temperatura = 'quente'

if temperatura == 'quente':
    print('Vamos tomar sorvete de flocos!')
    print('Vamos para a praia!')
else:
    print('Vamos comer chocolate!')
    print('Vamos ao cinema!')

## É maior ou igual
numero = 20

if numero > 20:
    print(f'{numero} é maior que 20.')
elif numero == 20:
    print(f'{numero} é igual a 20.')
else:
    print(f'{numero} não é maior que 20.')

## É diferente
nome = 'Mariana'

if(nome != 'Mariana'):
    print('Cadê a Mariana?')
else:
    print('É a Mariana!')

## Número da sorte
numero = 4

if numero == 1:
    print('Você ganhou!')
elif numero == 3:
    print('Você ganhou!')
elif numero == 5:
    print('Você ganhou!')
else:
    print('Você perdeu!')

## Testando duas condições
nome = 'Mariana'
sobrenome = 'Munari'

if nome == 'Mariana':
    if sobrenome == 'Munari':
        print('É a Mariana Munari!')
    else:
        print('É outra Mariana!')
else:
    print('Não é a Mariana Munari!')