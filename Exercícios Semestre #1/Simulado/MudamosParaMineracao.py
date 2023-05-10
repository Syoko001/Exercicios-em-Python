from time import sleep

def calcular_INR(pr, dt):
    if pr < 5:
        return pr * dt + 25 * dt
    elif pr >= 5 and pr < 10:
        return pr * pr + dt * dt
    else:
        return 80 * pr + 27 * dt


def calcular_IBN(pr, dt):
    qpar = 0
    s = 0
    for c in range(4):
        paridade = int(input(f'     Digite a {c + 1} paridade: '))
        s += paridade
    qpar = s / 4
    return INR * qpar


def calcular_classificacoes(pr, dt):
    if IBN < 10:
        return  '   Tipo visual: Filásia\n    Tipo de Resistência: Anotética'
    elif IBN >= 10 and IBN < 80:
        return '    Tipo visual: Tropitica\n    Tipo de Resistência: Blocada'
    else:
        return '    Tipo visual: Diamantada\n    Tipo de Resistência: Concredata'


poro_rocha = float(input('Digite a porosidade da rocha: '))
dens_rocha = float(input('Agora, digite a densidade da rocha: '))

INR = calcular_INR(poro_rocha, dens_rocha)
IBN = calcular_IBN(poro_rocha, dens_rocha)
classficacao_rocha = calcular_classificacoes(poro_rocha, dens_rocha)

print(f'O Índice de Nobreza da Rocha(INR) é: {INR}')
print(f'O Índice de Biparidade Normal(IBN) é: {IBN}')
print('Calculando...')
sleep(1.5)
print('='*50)
print(f'Classificação da rocha:\n{classficacao_rocha}')