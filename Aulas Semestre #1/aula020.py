def dobra(lst):
    pos = 0
    while pos < len(valores):
        lst[pos] *= 2
        pos += 1
    print(valores)

valores = [1, 3, 4, 2, 5, 4, 5]
print(valores)
dobra(valores)