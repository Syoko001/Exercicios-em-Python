#Um aluno de computação está organizando um bolão de futebol. Segundo suas regras, os apostadores informam o placar do jogo e ganham 10 pontos se acertarem o vencedor ou se foi empate. Ganham também mais 5 pontos para o placar de cada time que acertarem. Exemplo: se o placar do jogo foi 3x2, são 0 pontos se o placar apostado foi 0x1; 5 pontos para os placares apostados 0x2 ou 3x5; 10 pontos para o placar apostado 1x0; ou 20 pontos para o placar exato de 3x2. Faça um programa que requisita do usuário o placar apostado e depois o placar do jogo e informa quantos pontos o apostador fez.

aposta_usuario = input('Digite o seu palpite\033[30m(0x0)\033[m: ').split('x')
placar = input('Agora digite o placar do jogo\033[30m(0x0)\033[m: ').split('x')
maior_palpite = menor_palpite = 0
maior_placar = menor_placar = 0

#Verificação ponto maior e menor palpite
if int(aposta_usuario[0]) > int(aposta_usuario[1]):
    maior_palpite = menor_palpite = int(aposta_usuario[0])
    if menor_palpite > int(aposta_usuario[1]):
        menor_palpite = int(aposta_usuario[1])
    else:
        menor_palpite = int(aposta_usuario[0])
else:
    maior_palpite = menor_palpite = int(aposta_usuario[1])
    if menor_palpite > int(aposta_usuario[1]):
        menor_palpite = int(aposta_usuario[1])
    else:
        menor_palpite = int(aposta_usuario[0])

#Varificação Placar maior e menor
if int(placar[0]) > int(placar[1]):
    maior_placar = menor_placar = int(placar[0])
    if menor_placar > int(placar[1]):
        menor_placar = int(placar[1])
    else:
        menor_placar = int(placar[0])
else:
    maior_placar = menor_placar = int(placar[1])
    if menor_placar > int(placar[1]):
        menor_placar = int(placar[1])
    else:
        menor_placar = int(placar[0])

#verificações 10 pontos
if maior_palpite == menor_palpite and maior_placar == menor_placar:
    print('Empate, 10 pontos')
if maior_palpite == int(aposta_usuario[0]) and maior_placar == int(placar[0]):
    print('Time A vencedor, 10 pontos')
if maior_palpite == int(aposta_usuario[1]) and maior_placar == int(placar[1]):
    print('Time B vencedor, 10 pontos')
