idade = int(input('Digite sua idade: '))

categoria = 'Indefinida'

if(idade < 0 or idade > 200):
    print('Idade Invalida!!!')
elif(idade >= 20):
    categoria = 'Master'
elif(idade <= 9):
    categoria = 'Mirim'
elif(idade <= 14):
    categoria = 'Infantil'
elif(idade <= 19):
    categoria = 'Junior'
elif(idade <= 25):
    categoria = 'Senior'

print('A sua categoria e {}'.format(categoria))