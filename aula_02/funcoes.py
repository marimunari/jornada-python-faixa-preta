## Cálculo de Média
def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    print('O(a) aluno(a) ficou com média', media)
    verificar_aprovacao(media)


def verificar_aprovacao(media):
    if media >= 6:
        print('Situação: Aprovado(a)!')
    else:
        print('Situação: Reprovado(a)!')

notas = [ 10, 8, 9, 7]
media = calcular_media(notas)

## Cálculo de IMC
def numero_quadrado(numero):
    quadrado = numero ** 2
    return quadrado

def imc(peso, altura):
    altura_quadrada = altura ** 2
    calcIMC = peso / altura_quadrada
    return calcIMC

calcIMC = imc(47, 1.58)
print(f'IMC: {calcIMC:.2f}')