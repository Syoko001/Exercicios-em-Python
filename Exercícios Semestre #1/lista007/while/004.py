#Faça um algoritmo que determine o maior entre N números. A condição de parada é a entrada de um valor 0, ou seja, o algoritmo deve ficar calculando o maior até que a entrada seja igual a 0 (ZERO).

maior = menor = 0
numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))

    if numeros[len(numeros) - 1] == 0:
        break

    maior = max(numeros)
    menor = min(numeros)

print(f'Maior: {maior}\nMenor: {menor}')