distanciaEmKm = int(input('Digite quantos kms tera sua viagem: '))

if(distanciaEmKm <= 200):
    valor = distanciaEmKm * 0.5
else:
    valor = distanciaEmKm * 0.45
print('A sua viagem custara R${}'.format(valor))