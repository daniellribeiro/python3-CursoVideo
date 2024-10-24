from utilidadesCeV.cadastrarPessoa import cadastrarPessoa

while True:
    print('----------------------------------------')
    print('            MENU PRINCIPAL              ')
    print('----------------------------------------')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar  nova Pessoa')
    print('3 - Sair do sistema')
    print('----------------------------------------')
    try:
        opcao = int(input('Sua opcao: '))
        if opcao == 1:
            lista = cadastrarPessoa.lerArquivo()
            for dados in lista:
                print(f'{dados['nome'].ljust(15)} {dados['idade']:>3} anos')
        elif opcao == 2:
            nome = input('Digite seu nome: ')
            idade = input('Digite sua idade: ')
            if idade.isnumeric():
                cadastrarPessoa.salvarArquivo(nome,idade)
            else:
                print('Digite uma idade valida!!!')
        elif opcao == 3:
            print('Obrigado e volte sempre')
            break
        else:
            print('OPCAO INVALIDA')
    except:
        print('Opcao invalida!!!!')