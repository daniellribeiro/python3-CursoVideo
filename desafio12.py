#Desafio 12 - Ler preco do produto e mostrar seu preco com 5% de desconto

preco = float(input('Preco do produto: '))

print('Preco com 5 porcento de desconto: R$ {:.2f}'.format(preco - (preco*0.05)))