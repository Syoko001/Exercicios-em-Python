#Função que calcula area do tecido
def calcularArea(comprimento, largura):
    #Esse return atribui o valor da conta na varial que chama a função
    return comprimento * largura

#Função que calcula o valor total do tecido
def valorDeVenda(precoDoMetro, area):
    #Mesmo esquema do return anterior
    return precoDoMetro * area

#Condiciona a meta de venda, e verifica se o vendedor atingiu ou não a meta
def meta(totalDeVendas):
    if totalDeVendas > 5000:
        return 'Você atingiu a meta de vendas.'
    elif totalDeVendas > 3000 and totalDeVendas < 4999:
        return 'Você quase atingiu a meta de vendas. '
    elif totalDeVendas < 3000:
        return 'Você não atingiu a meta de vendas. '
    else:
        return 'Código inválido!' 


#Variaveis e listas que usei
contador = 0
vendedores = []
valorPorVenda = []

#Laço onde verifica se foram adicionados 10 vendedores no maximo, como diz o enunciado.
while True or contador != 9:
    #Adiciono os nomes do vendedores a uma lista pq futuramente vou precisar de todos ekes
    vendedores.append(input('Nome do vendedor(a): '))

    #Aqui verifica se no nome do vendedor o usuario digitou X que de acordo com o enunciado deve ser uma segunda condição de parada.
    if vendedores[contador] == 'x':
        break

    #Recendo informaçoes
    comprimento = float(input('Digite o comprimento: '))
    largura = float(input('Digite a largura: '))
    preco = float(input('Digite o preço: '))
    
    #Aqueles returns dentro das funções do começo fazem que aqueles valores venham para essas variaveis, cada um correspondente a variavel que chama a função
    area = calcularArea(comprimento, largura)
    totalAPagar = valorDeVenda(preco, area)
    valorPorVenda.append(totalAPagar)

    #printando as infomrações
    print(f'O valor de venda é: R${totalAPagar:.2f}')
    print(meta(totalAPagar))
    #Criei um contador para contar quantos vendedores foram adicionados, tbm funcionaria com o len no caso de lista
    contador += 1

#Mensagem bonitinha
print('='*30)
print('Relatótio de vendas')
print('='*30)

#Um laço finito para mostrar os vendedores e o valor que eles venderam
for index in range(0, contador):
    #Aqui mostra se foi a 1° venda ou a 2°
    print(f'Venda {index + 1}')
    #Aqui mostra o nome do vendedor e o valor de venda, cujo indice(index) esta relacionado na lista
    print(f'    Vendedor(a): {vendedores[index]}')
    print(f'    Total da venda: {valorPorVenda[index]}')
