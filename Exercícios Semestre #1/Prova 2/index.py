opcao = 0
nomes = ['Sandália', 'Camisa', 'Calça']
precos = [49.90, 79.90, 109.90]

def adicionarProduto():
    print('='*50)
    nomes.append(input('Nome do novo produto: '))
    precos.append(float(input('Valor do novo produto: ')))
    print('Produto cadastrado com sucesso!')
    print('='*50)


def consultarPrecoProduto(produto):
    for index, value in enumerate(nomes):
        if value == produto:
            return precos[index]
            


def calcularCompra(produto, quantidade):
    for index, value in enumerate(nomes):
        if value == produto:
            totCompra = precos[index] * quantidade

    if totCompra >= 100:
        return totCompra + (totCompra * 0.10)
    elif totCompra >= 50:
        return totCompra + (totCompra * 0.12)
    else:
        return totCompra + (totCompra * 0.15)

while opcao != 4:
    print("SISTEMA DE COMPRAS")
    print("1 - Adicionar Produto")
    print("2 - Consultar Preço Produto")
    print("3 - Calcular Compra")
    print("4 - Sair")

    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        adicionarProduto()
    elif opcao == 2:
        nomeProduto = input("Digite o nome do produto: ")
        preco = consultarPrecoProduto(nomeProduto)
        print(f"O preço do produto {nomeProduto} é {preco}")
    elif opcao == 3:
        nomeProduto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        valorTotal = calcularCompra(nomeProduto, quantidade)
        print(f"O valor total da compra é: {valorTotal:.2f}")
    elif opcao == 4:
        exit()
    else:
        print("Opção incorreta!")