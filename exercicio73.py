colocadosCampeonato = ('Flamengo', 'Palmeiras', 'São Paulo', 'Athletico PR', 'Atlético MG',
                       'Corinthians', 'Fluminense', 'Grêmio', 'Fortaleza', 'Chapecoense', 'Internacional',
                       'Bahia', 'Botafogo', 'Red Bull Bragantino', 'Atlético', 'Cuiabá',
                       'Vasco', 'Juventude', 'Criciúma', 'Vitória')

print('Os 5 primeiros colocados sao: ')
for i in colocadosCampeonato[0:5]:
    print(f'- {i}',end=' ')

print('\n')
print('Os 4 ultimos colocados sao: ')
for i in colocadosCampeonato[16:20]:
    print(f'- {i}',end=' ')

print('\n')
print('Ordem Alfabetica:')
for i in sorted(colocadosCampeonato):
    print(f'- {i}',end=' ')

print('\n')
print(f'Chapecoense esta na {colocadosCampeonato.index("Chapecoense") + 1}º posicao')