# Dada duas sequências com 4 números inteiros entre 0 e 9, calcular a sequência de números que representa a soma das sequências anteriores

vetor1 = [3, 5, 3, 5]
vetor2 = [8, 4, 2, 5]
vetorResultante = []

for contador in range(0, 4):
    vetorResultante.append(vetor1[contador] + vetor2[contador])

print(f'Vetor 1 =          {vetor1}')
print(f'Vetor 2 =          {vetor2}')
print(f'Vetor resultante = {vetorResultante}')