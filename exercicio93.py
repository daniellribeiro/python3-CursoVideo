jogador = {}
golsPartidas = []
jogador['totalGols'] = 0

jogador['nome'] = input('Digite seu nome: ')
jogador['numeroPartidas'] = int(input('QuantasPartidas vc jogou: '))
for i in range(jogador['numeroPartidas']):
    golsPartidas.append(int(input(f'Quantos gols vc fez na {i + 1} partida: ')))
    jogador['totalGols'] = jogador['totalGols'] + golsPartidas[i]
jogador['golsPartidas'] = golsPartidas

print(f'O jogador {jogador['nome']} jogou {jogador['numeroPartidas']} partidas')
for i in range(jogador['numeroPartidas']):
    print(f'=> Na partida {i+1}, fez {jogador['golsPartidas'][i]} gols')
print(f'Foi um total de {jogador['totalGols']} gols')