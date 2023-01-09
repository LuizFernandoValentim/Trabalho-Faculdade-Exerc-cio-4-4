listaProdutos = []
#Início do cadastro dos produtos
def cadastrarProduto(cod):
    print('Você selecionou a opção de Cadastrar Produto\n'
          'Código do produto {}'.format(cod))

    nome = input('Por favor entre com o nome do produto: ')
    fabricante = input('Por favor entre com o nome do fabricante: ')
    valor = input('Por favor entre com o valor R$: ')

    dicionarioProduto = {'Código': cod,
                         'Nome': nome,
                         'Fabricante': fabricante,
                         'Valor': valor}
    listaProdutos.append(dicionarioProduto.copy())
#Fim do cadastro dos produtos

#Início da consulta dos produtos
def consultarProduto():
    while True:
        try:
            print('Você selecionou a opção de Consultar Produto')

            opConsulta = int(input('1 - Consultar todos os produtos\n'
                  '2 - Consultar produtos por código\n'
                  '3 - Consultar produtos por fabricante\n'
                  '4 - Retornar\n'
                  'Escolha a opção desejada: '))

            if (opConsulta == 1):
                print('Bem-vindo a consulta de todos os produtos')
                for produto in listaProdutos:
                    for key, value in produto.items():
                        print('{} : {}'.format(key,value))

            elif (opConsulta == 2):
                print('Bem-vindo à consulta de produtos por código')
                entradaCod = int(input('Digite o código do produto: '))
                for produto in listaProdutos:
                    if (produto['Código'] == entradaCod):
                       for key, value in produto.items():
                         print('{} : {}'.format(key, value))

            elif (opConsulta == 3):
                print('Bem-vindo à consulta de produtos por fabricante')
                entradaFab = input('Digite o fabricante do produto: ')
                for produto in listaProdutos:
                    if (produto['Fabricante']  == entradaFab):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))

            elif (opConsulta == 4):
                break

            else:
                print('Código inválido. Tente novamente!')

                continue
        except ValueError:
            print('Pare de digitar valores não númericos. Tente novamente!')
            continue
#Fim da consulta dos produtos

#Início da função remover produtos
def removerProduto():
    print('Bem-vindo ao remover produtos')
    entradaRem = int(input('Digite o código do produto que deseja remover: '))
    for produto in listaProdutos:
        if (produto['Código'] == entradaRem):
            listaProdutos.remove(produto)
#Fim da função remover produtos

#Progama principal
print('Bem-vindo ao controle de estoque da Mercearia do Luiz Fernando Valentim (RU: 4173542)')
codProduto = 0
while True:
    try:
        opcao = int(input('1 - Cadastrar produto\n'
                          '2 - Consultar produtos\n'
                          '3 - Remover produto\n'
                          '4 - Sair\n'
                          'Digite a opção desejada: '))

    except ValueError:
        print('Pare de digitar valores não númericos. Tente novamente!')
        continue

    else:
        if (opcao == 1):
            codProduto += 1
            cadastrarProduto(codProduto)

        elif (opcao == 2):
            consultarProduto()

        elif (opcao == 3):
            removerProduto()

        elif (opcao == 4):
            print('O sistema está sendo finalizado...')
            break

        else:
            print('Código inválido. Tente novamente!')
            continue

