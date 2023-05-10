#Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) e informa se o resultado foi um empate, a vitória do primeiro time ou do segundo time.

time1 = input('Digite o nome do 1° time: ')
placar1 = int(input('Agora digite seu placar: '))
time2 = input('Digite o nome do 2° time: ')
placar2 = int(input('Agora digite seu placar: '))

if placar1 > placar2:
    vencedor = time1
else:
    vencedor = time2

print(f'''
\033[1;31m{time1}\033[m x \033[1;32m{time2}\033[m
\033[1;31m{placar1:<}\033[m - \033[1;32m{placar2:>}\033[m
''')
print(f'\033[1;37mO time vencedor é: \033[m{vencedor}')
