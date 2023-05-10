vet_nomes = ['Gustavo', 'Otacilio', 'Bruno V.', 'Bruno A.', 'Naksia', 'Rayssa', 'Pedro', 'Iago', 'Yago', 'Sr. Elias', 'Fernandao', 'Rayssa L.', 'Rayssa', 'Beatriz', 'Thiagão', 'Rodrigão', 'Kauan vulgo PK']
vet_bairros = ['Aroeiras', 'Acarape', 'Aeroporto', 'Água Mineral', 'Alegre', 'Alto Alegre', 'Parque Alvorada', 'Bom Jesus', 'Buenos Aires', 'Cidade Industrial', 'Embrapa', 'Itaperu', 'Parque Brasil', 'Mafrense', 'Mafuá', 'Matadouro', 'Memorare']
vet_idades = [32, 20, 51, 15, 51, 71, 14, 50, 43, 19, 27, 39, 10, 19, 57, 46, 30]
media_idades = sum(vet_idades) / len(vet_idades)


print(f'{len(vet_nomes)} Clientes cadastrados!')
print(f'A média de idades é de {media_idades:.2f} anos')


while True:
    busca = input('Buscar cliente: ')
    for index, nome in enumerate(vet_nomes):
        if nome in busca:
            print(f'{busca} tem {vet_idades[index]} anos!')
            print(f'E mora no bairro: {vet_bairros[index]}')

    continuar = input('Deseja continuar [s/n]: ').upper().strip()[0]
    if continuar in 'N':
        break

print('Obrigado, volte sempre')