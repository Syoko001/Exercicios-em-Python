n1 = input('Digite algo:')
print('Você digitou: {}'.format(n1))

print('É numérico? {}'.format(n1.isnumeric()))
print('É alphanumerico? {}'.format(n1.isalpha()))
print('É decimal? {}'.format(n1.isdecimal()))