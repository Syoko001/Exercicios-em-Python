# Dados dois vetores x e y, ambos com 5 elementos, determinar o produto escalar desses vetores.

x = [1, 3, 4, 2, 5]
y = [3, 5, 3, 5, 5]
resultado = []

for contador in range(0, 5):
    resultado.append(x[contador] * y[contador])

print(f'Vetor X = {x}')
print(f'Vetor y = {y}')
print(f'Result. = {resultado}')