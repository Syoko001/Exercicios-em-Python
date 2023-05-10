def calcularImc(peso, altura):
    return peso / altura**2


def situacao(resultado):
    if resultado >= 30:
        print('\033[1;31mEstado de obesidade.\033[m')
    elif resultado >= 25 and resultado <= 29.9:
        print('\033[1;33mVocê está acima de seu peso (sobrepeso).\033[m')
    elif resultado >= 18.5 and resultado <= 24.9:
        print('\033[1;32mParabéns! Você está em seu peso normal!\033[m')
    else:
        print('\033[1;33mVocê está abaixo do peso ideal.\033[m')


def titulo(pessoa):
    print(f'='*40)
    print(f'{pessoa:^40}')
    print(f'='*40)

for c in range(0, 5):
    titulo(f"Pessoa {c + 1}")
    nome = input('Nome: ')
    peso = float(input('Digite o peso: '))
    altura = float(input('Digite a altura: '))
    imc = calcularImc(peso, altura)
    print(f'O IMC dessa pessoa é de {imc:.2f}')
    situacao(imc)
