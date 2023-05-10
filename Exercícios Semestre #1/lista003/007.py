#Escreva um programa que leia 5 números, e imprima a média entre eles.

numeros = []
for c in range(1, 6):
    numeros.append(float(input('Digite um número: ')))

print('A média do número que você digitou é: {:.1f}'.format(sum(numeros)/len(numeros)))