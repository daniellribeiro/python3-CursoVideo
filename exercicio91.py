import random
lista = []
aleatorio = 0
contador = 1
for i in range(4):
    jogador = {'nome': input('Digite seu nome: '),
               'jogada': random.randint(1,6)
    }
    lista.append(jogador)

lista = sorted(lista,key=lambda x:x['jogada'], reverse=True)
print(lista)

print('Ranking: ')
print('Os ganhadores sao: ')
for i in lista:
    print(f'{i['nome']} esta em {contador} lugar')
    contador+=1