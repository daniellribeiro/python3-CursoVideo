jogadores = []
golsPartidas = []
numeroPartidas = 0
nome = ''

while True:
    golsPartidas = []
    nome = input('Digite seu nome: ')
    numeroPartidas = int(input('Quantas Partidas vc jogou: '))
    for i in range(numeroPartidas):
        golsPartidas.append(int(input(f'Quantos gols vc fez na {i + 1} partida: ')))

    jogador  = {'nome': nome,
                'numeroPartidas': numeroPartidas,
                'golsPartidas': golsPartidas,
                'totalGols': sum(golsPartidas)
                }
    jogadores.append(jogador)

    if input('Deseja continuar N - NAO S - SIM: ') in 'Nn':
        break

for jogador in jogadores:
    print('Codigo Nome             Gols             Total')
    print(f'{str(jogadores.index(jogador)).ljust(6)} {jogador['nome'].ljust(15) }  {str(jogador['golsPartidas']).ljust(15)}  {str(jogador['totalGols']).ljust(5)}')

while True:
    numero = int(input('Quer mostrar os dados de algum outro jogador 999 - Sair: '))
    if numero == 999:
        break
    if numero <= len(jogadores) and numero >= 0:
        print(f'O jogador {jogadores[numero]['nome']} jogou {jogadores[numero]['numeroPartidas']} partidas')
        for i in range(jogadores[numero]['numeroPartidas']):
            print(f'=> Na partida {i + 1}, fez {jogadores[numero]['golsPartidas'][i]} gols')
        print(f'Foi um total de {jogadores[numero]['totalGols']} gols')
    else:
        print('JOGADOR INVALIDO!!!')