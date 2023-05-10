#Crie um algoritmo que leia um número inteiro e imprima seu sucessor e seu antecessor.

print('\033[1;35m-=-\033[m'*20)
n = int(input('Digite um número inteiro: '))
print('\033[1;35m-=-\033[m'*20)

print('[ ANTECESSOR ]: {} \n [ NÚMERO ]: {} \n [ SUCESSOR ]: {}'.format(n - 1, n, n + 1))