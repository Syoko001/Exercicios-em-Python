#Desenvolva um programa imprime na tela os números entre 7 e 1000 que tem resto 3 quando divididos por 7.
num = 7
contador = 1

while num != 1001:
    if num % 7 == 3:
        print(num)
    num += 1