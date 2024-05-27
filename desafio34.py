salario = float(input('Digite o seu salario: '))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print('Seu aumento sera de R${:.2f}, seu salario passara a ser R${:.2f}'.format(aumento,salario + aumento))
