import os

opcao = 0
vet_nome = ['Rafael', 'João', 'José']
vet_bairro = ['Aeroporto', 'Zumbi', 'Amarelo']
vet_idade = [24, 37, 23]

def cadastrar_cliente():
    print()
    print('='*50, '\033[1;34m')
    print(f'{"Cadastro de novo cliente":^50}')
    print('\033[m')
    print('Preencha as informações requisitadas:')
    vet_nome.append(input('     Nome do Cliente: '))
    vet_bairro.append(input('     Bairro em que mora: '))
    vet_idade.append(int(input('     Idade do cliente: ')))
    print('\033[1;32mCliente cadastrado com sucesso!\033[m')
    print()


def buscar_bairro(nome_cliente):
    for index, nome in enumerate(vet_nome):
        if nome == busca:
            return vet_bairro[index]


def media_idade():
    return sum(vet_idade) / len(vet_idade)


while True:
    print('='*50)
    print(f'{"Vídeo Locadora do Fernandão":^50}')
    print('='*50)
    print(f'\033[30mVocê tem {len(vet_nome)} clientes cadastrados!\033[m')
    print('     [ 1 ] - Adicionar Clientes')
    print('     [ 2 ] - Procurar bairro do Cliente')
    print('     [ 3 ] - Exibir média de Idade')
    print('     [ 4 ] - Sair')
    print()

    opcao = input('Escolha uma das opções acima: ')
    os.system('cls')

    while True:

        if opcao in '1234':
            break
        else:
            print('Valor inválido tente novamente!')
            opcao = input('Escolha uma das opções acima: ') 

    if opcao in '1':
        cadastrar_cliente()

    elif opcao in '2':
        busca = input('Digite o nome do cliente que deseja consultar: ')
        busca_cliente = buscar_bairro(busca)

        print(f'O cliente requisitado mora no bairro \033[33m{busca_cliente}\033[m!')
    elif opcao in '3':
        print(f'A média de idade é \033[33m{media_idade()}\033[m')

    else:
        break

print('Sistema encerrado, até mais!')