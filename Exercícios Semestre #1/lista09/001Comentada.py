#Função que calcula o IMC com as informações de peso e altura da pessoa;
def calcularImc(peso, altura):

    #Essa função "return" faz retornar a uma variavel futura o valor introduzido a frente;
    #Exemplo: Da uma olhada la em baixo na variavel "IMC", ela ta recebendo o valor que chama a função "CalcularIMC" e dentro dessa função temos o real valor do IMC que é (peso / altura**2), o return só demonstra o valor real da função.
    return peso / altura**2

#Essa função "situação" quando chamada, mostra a situação do imc da pessoa. Se é: Obeso, sobrepeso, peso ideal e etc...
def situacao(resultado):

    #Os "if" trazem as condições, exemplo: se o resultado do imc for maior ou igual a 30, a pessoa ta em estado de obesidade.
    if resultado >= 30:
        print('Estado de obesidade.')
    #Se senão o resultado for maior ou igual a 25 e ao mesmo tempo resultador menor ou igual a 29.9, a pessoa está acima do peso.
    elif resultado >= 25 and resultado <= 29.9:
        print('Você está acima de seu peso (sobrepeso).')
    #Se senão o resultado do imc for maior ou igual a 18.5 e ao mesmo tempo for menor ou igual a 24.9 ele está no peso normal.
    elif resultado >= 18.5 and resultado <= 24.9:
        print('Parabéns! Você está em seu peso normal!')
    #Se não se encaixar em nenhuma das condições acima, ele vai mostrar que a pessoa ta no peso ideal.
    else:
        print('Você está abaixo do peso ideal.')


#Como no título pede a situação de 5 pessoas, eu criei um for in range para definir que ele vai contar de 0 a 5(lembrando que o ultimo numero sempre será desconsiderado. Ex: 0, 1, 2, 3, 4):
for c in range(0, 5):
    
    #Aqui mostra qual pessoa está sendo introduzida os dados.
    print(f'Pessoa {c + 1}')
    #Atribuição de variáveis só para receber os dados necessários.
    nome = input('Nome: ')
    peso = float(input('Digite o peso: '))
    altura = float(input('Digite a altura: '))
    #Nessa variável nós chamamos a primeira função do programa.
    imc = calcularImc(peso, altura)
    #printa o imc da pessoa.
    print(f'O IMC dessa pessoa é de {imc:.2f}')
    #Aqui chama a segunda função do programa.
    situacao(imc)
    #printando uma linha divisória, só para separar melhor as informações para a visualização do usuário;
    print('=-'*30)

#Lembrando, todas as funções só rodam dentro do programa quando são chamadas, caso não chamadas ficam "Inativas" no código.