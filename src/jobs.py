# -*- coding: utf-8 -*-
import csv
from functools import lru_cache

# 1 - Implemente a função read

# Para começarmos a processar os dados, devemos antes carregá-los
# em nossa aplicação.
# Esta função será responsável por abrir o arquivo CSV e
# retornar os dados no formato de uma lista de dicionários.

# A função deve receber um path (uma string com o caminho para um arquivo).
# A função deve abrir o arquivo e ler seus conteúdos.
# A função deve tratar o arquivo como CSV.
# A função deve retornar uma lista de dicionários, onde as chaves
# são os cabeçalhos de cada coluna e os valores correspondem a cada linha.


@lru_cache
def read(path):
    data = []
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in jobs_reader:
            data.append(row)

    return data
