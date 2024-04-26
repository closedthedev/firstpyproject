#criando um sorteador de times

import random

nomes = []

qnt_pessoas = int(input('Quantas pessoas terão em cada time: '))

# Solicitar os nomes dos jogadores
for i in range(1, (qnt_pessoas * 2) + 1):
    nome = input(f'Digite o nome do {i}º jogador: ').strip().title()
    nomes.append(nome)

# Embaralhar os jogadores na lista
random.shuffle(nomes)

# Dividir a lista em duas partes para formar os times
lista1 = nomes[:qnt_pessoas]
lista2 = nomes[qnt_pessoas:]

# Exibir os times sem colchetes e aspas
print('Time 1:', ', '.join(lista1))
print('Time 2:', ', '.join(lista2))