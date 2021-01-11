horario = 'manhã'
clima = 'ensolarado'
temperatura = 'quente'

if horario == 'manhã' or horario == 'tarde':
    if clima == 'ensolarado' and temperatura == 'quente':
        print('Que tal nadar em uma piscina?')
    if (clima == 'ensolarado' or clima == 'nublado') and (temperatura == 'amena' or temperatura == 'frio'):
        print('Talvez seja melhor praticar um esporte...')
    if clima == 'chuvoso':
        print('Acho que é bom ficar em casa e estudar!')
else:
    if clima == 'chuvoso':
        print('Hoje é melhor assitir um filme ou uma série!')
    else:
        print('Por que não jantar fora hoje?')