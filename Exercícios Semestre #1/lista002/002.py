#Elabore um algoritmo que comprove que: (x+y)² = x² + 2xy + y² para qualquer valor.

from time import sleep

print('\033[1;33m-=-\033[m'*20)
x = int(input('Atribua uma valor para X: '))
y = int(input('Atribua um valor para Y: '))
print('\033[1;33m-=-\033[m'*20)

print('Processando...')
sleep(1.5)

print('({}+{})² = {}² + 2.{}.{} + {}²'.format(x, y, x, x, y, y))
print('\033[1;33m-=-\033[m'*20)

direito = (x + y)**2
esquerdo = x **2 + 2 * x * y + y ** 2

print('O resultado da expressão é {} = {}'.format(direito, esquerdo))