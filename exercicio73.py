colocadosCampeonato = ('Flamengo', 'Palmeiras', 'São Paulo', 'Athletico PR', 'Atlético MG',
                       'Corinthians', 'Fluminense', 'Grêmio', 'Fortaleza', 'Chapecoense', 'Internacional',
                       'Bahia', 'Botafogo', 'Red Bull Bragantino', 'Atlético', 'Cuiabá',
                       'Vasco', 'Juventude', 'Criciúma', 'Vitória')

print(f'Os 5 primeiros colocados sao: {colocadosCampeonato[:5]} \n')

print(f'Os 4 ultimos colocados sao: {colocadosCampeonato[-4:]} \n')

print(f'Ordem Alfabetica:{sorted(colocadosCampeonato)} \n')

print(f'Chapecoense esta na {colocadosCampeonato.index("Chapecoense") + 1} º posicao')