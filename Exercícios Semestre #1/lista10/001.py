def calcularArea(comprimento, largura):
    return comprimento * largura

def valorDeVenda(precoDoMetro, area):
    return precoDoMetro * area

def meta(totalDeVendas):
    if totalDeVendas > 5000:
        return 'Você atingiu a meta de vendas.'
    elif totalDeVendas > 3000 and totalDeVendas < 4999:
        return 'Você quase atingiu a meta de vendas. '
    elif totalDeVendas < 3000:
        return 'Você não atingiu a meta de vendas. '
    else:
        return 'Código inválido!' 


contador = 0
vendedores = []
valorPorVenda = []

while True or contador != 9:
    vendedores.append(input('Nome do vendedor(a): '))

    if vendedores[contador] == 'x':
        break

    comprimento = float(input('Digite o comprimento: '))
    largura = float(input('Digite a largura: '))
    preco = float(input('Digite o preço: '))
    
    area = calcularArea(comprimento, largura)
    totalAPagar = valorDeVenda(preco, area)
    valorPorVenda.append(totalAPagar)

    print(f'O valor de venda é: R${totalAPagar:.2f}')
    print(meta(totalAPagar))
    contador += 1

print('='*30)
print('Relatótio de vendas')
print('='*30)

for index in range(0, contador):
    print(f'Venda {index + 1}')
    print(f'    Vendedor(a): {vendedores[index]}')
    print(f'    Total da venda: {valorPorVenda[index]}')
