#condições

nome = str(input('Digite seu nome: ')).strip()

if nome == 'Murillo':
    print('Que nome lindo você tem. <3')
else:
    print('Que nome chato -_-')
print('Bom dia, {}'.format(nome))
