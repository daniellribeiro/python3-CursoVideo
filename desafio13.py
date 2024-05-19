#Desafio 13 - Ler salario do funcionario e calcular o salario com 15% de aumento

salario = float(input('Salario do funcionario: '))

print('salario com 15 porcento de aumento: R$ {:.2f}'.format(salario + (salario*0.15)))