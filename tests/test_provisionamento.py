import csv

from src.services.provisionamento_service import ProvisionamentoService


def test_processar():
    caminho = "data/unidades.csv"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        quantidade_unidades = sum(1 for _ in csv.DictReader(arquivo))

    ps = ProvisionamentoService()
    resultado = ps.processar(caminho)

    assert "unidades" in resultado
    assert "falhas" in resultado

    assert (
        len(resultado["unidades"]) + len(resultado["falhas"])
        == quantidade_unidades
    )