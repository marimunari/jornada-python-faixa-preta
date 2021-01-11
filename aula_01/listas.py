## Dados Sequenciais em Python
animais = ['Gato', 'Cachorro', 'Coelho', 'Furão', 'Hamster']

## Exibindo dados da lista
print('O Meowth é um', animais[0])
print('O Bolt é um', animais[1])
print('O Pernalonga é um', animais[2])
print('O Axe é um', animais[3])
print('O Stuart é um', animais[4])

## Lista aninhada
lista = [[1,2], [3,4], [5,6]]

## Exibindo a primeira sublista
primeiraSub = lista[0]
print(primeiraSub)

## Exibindo o primeiro número da primeira sublista
primeiroNum = primeiraSub[0]
print(primeiroNum)

## Exibindo o segundo número da segunda sublista
segundaSub = lista[1][1]
print(segundaSub)

## Criando uma lista vazia
listaVazia = []

## Adicionando dados na lista
listaVazia.append('Mariana')
listaVazia.append(20)

print(f'A {listaVazia[0]} tem {listaVazia[1]} anos')
