#Dada sequência de 10 números inteiros, imprimi-la na ordem inversa à da leitura

# 1° forma com for

for numero in range(10, 0, -1):
    print(numero)



# 2° forma com while

numero = 10

while True:
    print(numero)
    numero -= 1
    if numero == 0:
        break