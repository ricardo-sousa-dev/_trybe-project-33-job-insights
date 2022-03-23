# espera-se que a pessoa usuária possa escolher um critério de
# ordenação para exibir os empregos. Já temos uma implementação
#  para essa ordenação em src/sorting.py, mas queremos ter certeza
#  de que ela funciona e, principalmente, que não deixará de
# funcionar conforme vamos implementando novos recursos.
# Precisamos então escrever um teste!

# Esse teste deve se chamar test_sort_by_criteria e garantir
# que a função funciona segundo esta especificação:

# A função sort_by recebe dois parâmetros:
# jobs uma lista de dicionários com os detalhes de cada emprego;
# criteria uma string com uma chave para ser usada como critério de ordenação.
# O parâmetro criteria deve ter um destes valores: min_salary,
#  max_salary, date_posted
# A ordenação para min_salary deve ser crescente, mas para max_salary
#  ou date_posted devem ser decrescentes.
# Os empregos que não apresentarem um valor válido no campo escolhido
#  para ordenação devem aparecer no final da lista.
# 📌 O teste da Trybe espera que o seu teste falhe em alguns casos.
#  Nesse caso, o teste terá a saída XFAIL (ao invés de PASS ou FAIL),
# e isso significa que o requisito foi atendido ✔️

from src.sorting import sort_by
import pytest

# Simula um registro sem data de criação
invalid_keys = ["date_create", None]

jobs = [
    {"max_salary": 83891, "min_salary": 73558, "date_posted": "2022-02-07"},
    {"max_salary": 116224, "min_salary": 57432, "date_posted": "2022-03-25"},
    {"max_salary": 125003, "min_salary": 98266, "date_posted": "2022-01-15"},
]

# dicionário de jobs após a ordenação por min_salary
# - usado para comparação no teste
expected_min_salary = [
    {"max_salary": 116224, "min_salary": 57432, "date_posted": "2022-03-25"},
    {"max_salary": 125003, "min_salary": 98266, "date_posted": "2022-01-15"},
    {"max_salary": 83891, "min_salary": 73558, "date_posted": "2022-02-07"},
]

# dicionário de jobs após a ordenação por max_salary
# - usado para comparação no teste
expected_max_salary = [
    {"max_salary": 125003, "min_salary": 98266, "date_posted": "2022-01-15"},
    {"max_salary": 116224, "min_salary": 57432, "date_posted": "2022-03-25"},
    {"max_salary": 83891, "min_salary": 73558, "date_posted": "2022-02-07"},
]

# dicionário de jobs após a ordenação por date_posted
# - usado para comparação no teste
expected_date_post = [
    {"max_salary": 116224, "min_salary": 57432, "date_posted": "2022-03-25"},
    {"max_salary": 83891, "min_salary": 73558, "date_posted": "2022-02-07"},
    {"max_salary": 125003, "min_salary": 98266, "date_posted": "2022-01-15"},
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == expected_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == expected_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == expected_date_post

    for criteria in invalid_keys:
        with pytest.raises(ValueError, match=f"Sorting invalid to {criteria}"):
            sort_by(jobs, criteria)

# https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=raises#pytest.raises
# https://docs.pytest.org/en/7.1.x/example/simple.html?highlight=assert
