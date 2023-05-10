#Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem: “Múltiplo de 10”.

num = 1

while num != 101:
    if num % 10 == 0:
        print(f'Múltiplo de 10: {num}')
    else:
        print(num)
    num += 1