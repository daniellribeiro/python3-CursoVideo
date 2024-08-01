numero = int(input('Digite um numero: '))
i = 0
numero1 = 0
numero2 = 1
soma = 0

while i < numero:
    if i == 0 or i == 1:
        print('{}, '.format(i),end='')
    else:
      soma = numero1 + numero2
      print('{}, '.format(soma), end='')
      numero1 = numero2
      numero2 = soma
    i += 1
print('FIM')