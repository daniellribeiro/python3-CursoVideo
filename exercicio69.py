idade = 0
sexo = ''
contadorMais18anos = 0
contadorSexoMasculino = 0
contadorSexoFIdadeMenor20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite o sexo F-feminino / M-masculino: ')
    if idade >= 18:
        contadorMais18anos += 1
    if sexo in 'Mm':
        contadorSexoMasculino += 1
    if sexo in 'Ff' and idade < 20:
        contadorSexoFIdadeMenor20 += 1

    if int(input('Deseja continuar 0 - SIM / 1 - NAO: ')) == 1:
        break
print(f'Tem {contadorMais18anos} pessoas com mais de 18 anos')
print(f'Tem {contadorSexoMasculino} homens')
print(f'Tem {contadorSexoFIdadeMenor20} mulheres com menos de 20 anos')