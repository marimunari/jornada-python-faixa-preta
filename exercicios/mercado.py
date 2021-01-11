frutas = ['Maçã', 'Banana', 'Pera', 'Uva']
guloseimas = ['Bolacha', 'Batata', 'Fini', 'Chocolate']
comidas = ['Arroz', 'Feijão', 'Carne']
bebidas = ['Refrigerante', 'Suco de Morango', 'Água']

categorias = ['Frutas', 'Guloseimas', 'Comidas', 'Bebidas']
compras = [frutas, guloseimas, comidas, bebidas]

for indice, categoria in enumerate(categorias):
    print('Você precisa comprar', len(compras[indice]), categoria+':')
    for compra in compras[indice]:
        print('-', compra)