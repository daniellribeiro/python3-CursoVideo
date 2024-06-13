
precoProduto = float(input('Digite o valor do produto: '))

print('Valor a vista dinheiro / cheque R${:.2f}'.format(precoProduto - (precoProduto * 0.1)))

print('Valor a vista no cartao R${:.2f}'.format(precoProduto - (precoProduto * 0.05)))

print('Valor em ate 2 vezes no cartao R${}'.format(precoProduto))

print('Valor em ate 3 vezes ou mais no cartao R${}'.format(precoProduto + (precoProduto * 0.2)))


if int(input('Voce passara no cartao credito ? : 1 - SIM / 0 - NAO: ')) == 1:
    parcelas = int(input('Em quantas parcelas ? '))
    if(parcelas < 3):
        precoProdutoCartao = precoProduto
    else:
        precoProdutoCartao = precoProduto + (precoProduto * 0.2)

    print('Ficara {}X de R${:.2f}'.format(parcelas, precoProdutoCartao / parcelas))
