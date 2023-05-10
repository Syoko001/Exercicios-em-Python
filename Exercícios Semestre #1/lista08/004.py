# faça um algoritmo que armazene em um vetor de caracteres todas as vogais. Posteriormente esse algoritmo deve exibir na tela todas as vogais da seguite forma: a ae aei aeio aeiou

vogais = ['a', 'e', 'i', 'o', 'u']
vetorX = []

for contador in range(0, 5):
    vetorX.append(vogais[contador])
    for index, vogal in enumerate(vetorX):
        print(vogal, end='')
    print()