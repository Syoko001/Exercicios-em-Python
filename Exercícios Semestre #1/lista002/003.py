#Criar um algoritmo que calcule e imprima a área de um triângulo.

from email.mime import base


print('\033[1;32m-=-\033[m'*20)
base1 = float(input('Digite valor da base: '))
altura = float(input('Digite a altura: '))
print('\033[1;32m-=-\033[m'*20)

area = base1 * altura / 2

print('O valor da área do triângulo é \033[33m{}\033[m'.format(area))