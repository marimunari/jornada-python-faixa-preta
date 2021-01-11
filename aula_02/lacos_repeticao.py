## Laço FOR
## Exibindo os números em sequência
for numero in range(10):
    print('O número atual é:', numero)

## Exibindo os números limitando de 3 a 9
for numero in range(3, 9):
    print(numero)

## Exibindo os números de 2 em 2
for numero in range(3, 16, 2):
    print(numero)

## Laço FOR com IF
for numero in range(1, 11):
    if numero % 2 == 0:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é impar!')

## Laço FOR com listas
notas = [10, 8, 9, 7, 5]
soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)

print('A média é igual a', media)

## Alternativa para o exemplo de laço FOR com listas
notas = [10, 8, 9, 7, 5]
soma = sum(notas)
media = soma / len(notas)

print('A média é igual a', media)