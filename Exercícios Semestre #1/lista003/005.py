#Faça um programa para exibir uma lista de compras de supermercado com 6 ítens. Exiba a lista logo após. Utilize vetores.

compras = []

print('\033[34m=\033[m'*10, ' LISTA DE COMPRAS ', '\033[34m=\033[m'*10)
print('\033[30mDigite os produtos que precisa levar.\033[m')

for c in range(1,7):
    compras.append(str(input('\033[1;33m-\033[mDigite o produto: ')))

print('''Eis a sua lista:
{}'''.format(compras))