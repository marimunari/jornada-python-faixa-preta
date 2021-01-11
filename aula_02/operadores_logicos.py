## Condições E (and): Todas devem ser verdadeiras
nome = 'Mariana'
sobrenome = 'Munari'
idade = 20

if nome.lower() == 'mariana' and sobrenome.lower() == 'munari'and idade == 20:
    print('É a Mariana Munari!')
else:
    print('É outra Mariana!')

## Condição OU (or): Pelo menos um
numero = 4

if numero == 1 or numero == 3 or numero == 5:
    print('Você ganhou!')
else:
    print('Você perdeu!')

## Utilizando dois operadores
nome = 'Mariana'
numero = 3

if nome == 'Mariana' and (numero == 1 or numero == 3 or numero == 5):
    print('A Mariana escolheu o número certo!')
else:
    print('Erro')

## Utilizando listas
numeros = [1, 3, 5, 7, 9]
numero = 5

if numero in numeros:
    print('Você ganhou!')
else:
    print('Você perdeu!')
