#Crie um algoritmo que recebe o nome de um aluno, o telefone e sua idade. A partir destas informações você deverá imprimir as seguintes frases:
#“Aluno: <nome do aluno> ”
#“Telefone: <número do telefone>”
#“Maior de 18 anos: <verdadeiro ou falso>”

print('\033[1;37m-=-\033[m'*20)

nome = str(input('Digite seu nome completo: ')).strip()
telefone = int(input('Digite seu número de telefone: '))
idade = int(input('Digite sua idade: '))

print('\033[1;37m-=-\033[m'*20)

print('ALUNO: <{}>'.format(nome))
print('TELEFONE: <{}>'.format(telefone))
print('MAIOR DE 18: <{}>'.format(idade > 18))