print('Calculadora da ByLearn\n')

## Entrada dos dados
primeiroNum = float(input('Digite o 1º número: '))
segundoNum = float(input('Digite o 2º número: '))

## Operações matemáticas
soma = primeiroNum + segundoNum
subtracao = primeiroNum - segundoNum
multiplicacao = primeiroNum * segundoNum
divisao = primeiroNum / segundoNum

## Saída de dados
print(f'\nSoma:\n {primeiroNum} + {segundoNum} = {soma}')
print(f'\nSubtração:\n {primeiroNum} - {segundoNum} = {subtracao}')
print(f'\nMultiplicação:\n {primeiroNum} * {segundoNum} = {multiplicacao}')
print(f'\nDivisão:\n {primeiroNum} / {segundoNum} = {divisao}')