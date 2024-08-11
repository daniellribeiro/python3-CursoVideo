descricaoProduto = ''
precoProduto = 0
soma = 0
produtosMais1000 = 0
precoProdutoMaisBarato = 0
descricaoProdutoMaisBarato = ''
while True:
    descricaoProduto = input('Digite o nome do produto: ')
    precoProduto = float(input('Digite o preco do produto: '))

    if precoProduto > 1000:
        produtosMais1000 += 1
    if precoProduto < precoProdutoMaisBarato or soma == 0:
        precoProdutoMaisBarato = precoProduto
        descricaoProdutoMaisBarato = descricaoProduto
    soma += precoProduto

    if(int(input('Deseja continuar 0-SIM / 1-NAO: '))==1):
        break
print(f'O total gasto e {soma:.2f}')
print(f'{produtosMais1000} produtos custaram mais de 1000 reais')
print(f'O produto mais barato se chama {descricaoProdutoMaisBarato}, e custou {precoProdutoMaisBarato}')