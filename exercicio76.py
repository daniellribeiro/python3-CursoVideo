produtos=('arroz','18.79',
          'feijao','7.98',
          'leite','4.98',
          'alface','2.37')

for i in range(0,len(produtos),2):
    print(f'{produtos[i].ljust(10,'.')}R${produtos[i+1].rjust(6,' ')}')