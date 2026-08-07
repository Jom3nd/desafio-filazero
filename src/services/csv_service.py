import csv

def read(path: str) -> list[dict]:

    unidades = []

    with open(path, mode="r", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            unidades.append(linha)

        return unidades