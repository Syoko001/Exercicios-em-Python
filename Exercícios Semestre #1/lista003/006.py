#Escreva um programa para gerar o invertido de um número com três algarismos (exemplo: o invertido de 498 é 894).
from random import randint
from time import sleep

print('Aleatorizando um número...')
sleep(1.5)
numero = randint(100, 999)

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print('Número gerado: {}'.format(numero))
print('O mesmo número invertido é: {}{}{}'.format(unidade, dezena, centena))