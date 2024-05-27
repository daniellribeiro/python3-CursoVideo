#Fatiamento
frase = 'Curso em video python'

print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Analise
print('Analise')
print(len(frase))
print(frase.count('o'))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

#Transformacao
print('Transformacao')
print(frase.replace('python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print('    Teste    '.strip())
print('    Teste    '.rstrip())
print('    Teste    '.lstrip())
print(frase.split())
frase2 = frase.split()
print('-'.join(frase2))
print('''Teste
Teste
Teste''')