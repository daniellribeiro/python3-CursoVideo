pessoas = [['Daniel',90.5],
           ['Jose',100.1],
           ['Teste',50.94]]
pessoasPesoCresc = []
pessoasPesoDescr = []

for nome,peso in pessoas:
    print(f'{nome} pesa {peso} Kg')

pessoasPesoCresc = sorted(pessoas, key=lambda x: x[1])
pessoasPesoDescr  = sorted(pessoas, key=lambda x: x[1], reverse=True)

print('Crescente:')
for nome,peso in pessoasPesoCresc:
    print(f'{nome} pesa {peso} Kg')

print('Decrescente:')
for nome,peso in pessoasPesoDescr:
    print(f'{nome} pesa {peso} Kg')
