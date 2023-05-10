#Faça um algoritmo para Calcular a área do trapézio ilustrado na figura, sabendo-se que esta área pode ser calculada pela expressão algébrica A=(B+b)×h/2, onde B é a medida da base maior, b é a medida da base menor e h é a medida da altura. (Seu programa deve receber os valores de b, h e B diretos do usuário).

b = 4
h = 3
B = 9

print('\033[1;34m-=-\033[m'*20)
print('Com os valores: \n [ ALTURA ]: \033[33m{}\033[m \n [ BASE ]: \033[33m{}\033[m \n [ TOPO ]: \033[33m{}\033[m'.format(h, B, b))
print('Então a área do trapézio é \033[1;33m{}\033[m.'.format((B + b) * h/2 ))