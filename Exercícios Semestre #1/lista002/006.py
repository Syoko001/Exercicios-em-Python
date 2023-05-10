#Entrar com dois números e imprimir a seguinte saída:
#dividendo
#divisor
#quociente
#resto

print('\033[1;33m-=-\033[m'*30)

n1 = float(input('Digite um \033[33mnúmero\033[m: '))
n2 = float(input('Digite mais um \033[33mnúmero\033[m: '))

print('\033[1;33m-=-\033[m'*30)

print('Entre a divisão de {} e {}:'.format(n1, n2))
print('O DIVIDENDO é: {}'.format(n1))
print('O DIVISOR é: {}'.format(n2))
print('O QUOCIENTE é: {}'.format(n1 / n2))
print('O RESTO da divisão é: {}'.format(n1 % n2))