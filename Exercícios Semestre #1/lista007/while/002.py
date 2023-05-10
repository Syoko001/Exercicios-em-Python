#Desenvolva um algoritmo que obtêm números do usuário e os soma. A cada repetição o algoritmo deve perguntar ao usuário se o mesmo deseja continuar a digitar números. Enquanto o usuário digitar “s” o algoritmo continua a receber números e somá-los. Quando o usuário digita qualquer outra coisa o algoritmo termina.

soma = 0

while True:
    numero = int(input('Digite um número: '))
    soma += numero

    continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]

    if continuar not in 'SN':
        print('Valor inválido, tente novamente!')
        continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]

    if continuar in 'N':
        break

print(f'A soma dos numeros digitados é: {soma}')