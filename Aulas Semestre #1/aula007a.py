#solicite os digitos

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

#soma, subtração, divisão, multiplicação, potênciação, resto, divisão inteira

s = n1 + n2
sub = n1 - n2
d = n1 / n2
m = n1 * n2
p = n1 ** n2
r = n1 % n2
di = n1 // n2

#print dos resultados

print('{0} + {1} = {2}'.format(n1, n2, s))
print('{} - {} = {}'.format(n1, n2, sub))
print('{} / {} = {:.3f}'.format(n1, n2, d))
print('O resto da divisão entre {} e {} é: {}'.format(n1, n2, r))
print('{} x {} = {}'.format(n1, n2, m))
print('{}**{} = {}'.format(n1, n2, p))
print('A divisão inteira de {} e {} é: {}'.format(n1, n2, di))