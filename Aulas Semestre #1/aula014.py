#while

n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par += 1
    elif n % 2 == 1:
        impar += 1
    
print('Acabou')
print('{} números pares digitados.'.format(par))
print('{} números ímpares foram digitados.'.format(impar))